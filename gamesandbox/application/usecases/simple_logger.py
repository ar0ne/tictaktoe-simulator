from logging import Logger
from typing import Any


class SimpleLogger:
    """
    Dummy logger that just wraps logging Logger
    """

    def __init__(self, logger: Logger) -> None:
        self._logger = logger

    def debug(self, msg: Any, *args, **kwargs) -> None:
        self._logger.debug(msg, *args, **kwargs)

    def info(self, msg: Any, *args, **kwargs) -> None:
        self._logger.info(msg, *args, **kwargs)

    def warning(self, msg: Any, *args, **kwargs) -> None:
        self._logger.warning(msg, *args, **kwargs)

    def error(self, msg: Any, *args, **kwargs) -> None:
        self._logger.error(msg, *args, **kwargs)
