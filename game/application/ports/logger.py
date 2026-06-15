from typing import Protocol, Any


class ILogger(Protocol):

    def debug(self, msg: Any, *args, **kwargs) -> None:
        ...

    def info(self, msg: Any, *args, **kwargs) -> None:
        ...

    def warning(self, msg: Any, *args, **kwargs) -> None:
        ...

    def error(self, msg: Any, *args, **kwargs) -> None:
        ...
