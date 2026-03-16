import enum
import io
import json
from dataclasses import dataclass
from typing import Any, BinaryIO, Callable, Union

_ACTIVE_BACKEND = "json"


class AvailableBackends(enum.Enum):
    JSON = "json"
    MSGSPEC = "msgspec"
    IJSON = "ijson"


# Define what a backend looks like
@dataclass
class JSONBackend:
    load: Callable[[BinaryIO], Any]
    loads: Callable[[Union[bytes, str]], Any]


AVAILABLE_BACKENDS: dict[str, JSONBackend] = {}


# 1. Standard Library
def _stdlib_load(fp: BinaryIO) -> Any:
    return json.load(fp)


def _stdlib_loads(data: Union[bytes, str]) -> Any:
    return json.loads(data)


AVAILABLE_BACKENDS[AvailableBackends.JSON.value] = JSONBackend(
    load=_stdlib_load, loads=_stdlib_loads
)


# 2. msgspec
try:
    import msgspec

    def _msgspec_load(fp: BinaryIO) -> Any:
        return msgspec.json.decode(fp.read())

    def _msgspec_loads(data: Union[bytes, str]) -> Any:
        return msgspec.json.decode(data)

    AVAILABLE_BACKENDS[AvailableBackends.MSGSPEC.value] = JSONBackend(
        load=_msgspec_load, loads=_msgspec_loads
    )
except ImportError:
    pass


# 3. ijson
try:
    import ijson

    def _ijson_load(fp: BinaryIO) -> Any:
        for item in ijson.items(fp, ""):
            return item
        return {}

    def _ijson_loads(data: Union[bytes, str]) -> Any:
        # ijson needs a file-like object and prefers bytes
        if isinstance(data, str):
            data = data.encode("utf-8")
        for item in ijson.items(io.BytesIO(data), ""):
            return item
        return {}

    AVAILABLE_BACKENDS[AvailableBackends.IJSON.value] = JSONBackend(
        load=_ijson_load, loads=_ijson_loads
    )
except ImportError:
    pass


def set_json_backend(name: str) -> None:
    """Globally configure which JSON backend sc2_datasets uses."""
    global _ACTIVE_BACKEND
    if name not in AVAILABLE_BACKENDS:
        raise ValueError(
            f"Backend '{name}' is not installed or available. "
            f"Available backends: {list(AVAILABLE_BACKENDS.keys())}"
        )
    _ACTIVE_BACKEND = name


def get_json_backend() -> str:
    """Return the name of the currently active JSON backend."""
    return _ACTIVE_BACKEND


# 5. Unified Proxy Methods for internal use
def load(fp: BinaryIO) -> Any:
    """Parse JSON from a file-like object using the active backend."""
    return AVAILABLE_BACKENDS[_ACTIVE_BACKEND].load(fp)


def loads(data: Union[bytes, str]) -> Any:
    """Parse JSON from bytes or a string using the active backend."""
    return AVAILABLE_BACKENDS[_ACTIVE_BACKEND].loads(data)
