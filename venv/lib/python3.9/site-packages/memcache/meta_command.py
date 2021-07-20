from dataclasses import dataclass
from typing import List, Optional, Union


@dataclass(init=False)
class MetaCommand:
    cm: bytes
    key: bytes
    flags: List[bytes]
    value: Optional[bytes]

    def __init__(
        self,
        cm: bytes,
        key: Union[bytes, str],
        flags: List[bytes],
        value: Optional[bytes],
    ) -> None:
        if isinstance(key, str):
            key = key.encode()
        self.cm = cm
        self.key = key
        self.flags = flags
        self.value = value


@dataclass
class MetaResult:
    rc: bytes
    flags: List[bytes]
    value: Optional[bytes]
