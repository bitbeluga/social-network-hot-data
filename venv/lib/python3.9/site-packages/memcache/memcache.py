import socket
from typing import Any, List, Optional, Tuple, Union

from .errors import MemcacheError
from .meta_command import MetaCommand, MetaResult
from .serialize import dump, load, DumpFunc, LoadFunc


NEWLINE = b"\r\n"


class Connection:
    def __init__(
        self,
        addr: Union[Tuple[str, int]],
        *,
        load_func: LoadFunc = load,
        dump_func: DumpFunc = dump
    ):
        self._addr = addr
        self._load = load_func
        self._dump = dump_func
        self._connect()

    def _connect(self) -> None:
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(self._addr)
        self.stream = self.socket.makefile(mode="rwb")

    def close(self) -> None:
        self.stream.close()
        self.socket.close()

    def flush_all(self) -> None:
        self.stream.write(b"flush_all\r\n")
        self.stream.flush()
        response = self.stream.readline()
        if response != b"OK\r\n":
            raise MemcacheError(response.removesuffix(NEWLINE))

    def execute_meta_command(self, command: MetaCommand) -> MetaResult:
        try:
            return self._execute_meta_command(command)
        except (IndexError, ConnectionResetError, BrokenPipeError):
            # This happens when connection is closed by memcached.
            self._connect()
            return self._execute_meta_command(command)

    def _execute_meta_command(self, command: MetaCommand) -> MetaResult:
        header = b" ".join([command.cm, command.key] + command.flags + [b"\r\n"])
        self.stream.write(header)
        if command.value:
            self.stream.write(command.value + b"\r\n")
        self.stream.flush()
        return self._receive_meta_result()

    def _receive_meta_result(self) -> MetaResult:
        header = self.stream.readline()
        parts = header.split()
        rc = parts[0]
        flags = parts[1:]
        value = None
        if rc == b"VA":
            size = int(parts[1])
            flags = parts[2:]
            value = self.stream.read(size)
            self.stream.read(2)  # read the "\r\n"
        return MetaResult(rc=rc, flags=flags, value=value)

    def set(
        self, key: Union[bytes, str], value: Any, expire: Optional[int] = None
    ) -> None:
        value, client_flags = self._dump(key, value)

        flags = [b"S%d" % len(value), b"F%d" % client_flags]
        if expire:
            flags.append(b"T%d" % expire)

        command = MetaCommand(cm=b"ms", key=key, flags=flags, value=value)
        self.execute_meta_command(command)

    def get(self, key: Union[bytes, str]) -> Optional[Any]:
        command = MetaCommand(cm=b"mg", key=key, flags=[b"v", b"f"], value=None)
        result = self.execute_meta_command(command)

        if result.value is None:
            return None

        client_flags = int(result.flags[0][1:])

        return self._load(key, result.value, client_flags)

    def delete(self, key: Union[bytes, str]) -> None:
        command = MetaCommand(cm=b"md", key=key, flags=[], value=None)
        self.execute_meta_command(command)


Addr = Tuple[str, int]


class Memcache:
    def __init__(
        self,
        addr: Union[Addr, List[Addr]] = None,
        *,
        load_func: LoadFunc = load,
        dump_func: DumpFunc = dump
    ):
        addr = addr or ("localhost", 11211)
        if isinstance(addr, list):
            self.connections = [
                Connection(x, load_func=load_func, dump_func=dump_func) for x in addr
            ]
        else:
            self.connections = [
                Connection(addr, load_func=load_func, dump_func=dump_func)
            ]

    def _get_connection(self, key) -> Connection:
        return self.connections[hash(key) % len(self.connections)]

    def execute_meta_command(self, command: MetaCommand) -> MetaResult:
        return self._get_connection(command.key).execute_meta_command(command)

    def flush_all(self) -> None:
        for connection in self.connections:
            connection.flush_all()

    def set(
        self, key: Union[bytes, str], value: Any, *, expire: Optional[int] = None
    ) -> None:
        return self._get_connection(key).set(key, value, expire=expire)

    def get(self, key: Union[bytes, str]) -> Optional[Any]:
        return self._get_connection(key).get(key)

    def delete(self, key: Union[bytes, str]) -> None:
        return self._get_connection(key).delete(key)
