import pickle
from typing import Any, Callable, Tuple, Union

from .errors import SerializeError


FLAG_BYTES = 0
FLAG_PICKLE = 1 << 0
FLAG_INT = 1 << 1
FLAG_STR = 1 << 4


DumpFunc = Callable[[Union[str, bytes], Any], Tuple[bytes, int]]


def dump(key: Union[str, bytes], value: Any) -> Tuple[bytes, int]:
    if isinstance(value, bytes):
        return value, FLAG_BYTES
    elif isinstance(value, int):
        return b"%d" % value, FLAG_INT
    elif isinstance(value, str):
        return value.encode(), FLAG_STR
    return pickle.dumps(value), FLAG_PICKLE


LoadFunc = Callable[[Union[str, bytes], bytes, int], Any]


def load(key: Union[str, bytes], value: bytes, flags: int) -> Any:
    if flags == FLAG_BYTES:
        return value
    elif flags == FLAG_INT:
        return int(value)
    elif flags == FLAG_STR:
        return value.decode()
    elif flags == FLAG_PICKLE:
        return pickle.loads(value)
    else:
        raise SerializeError(f"Unrecognized flags: {flags}")
