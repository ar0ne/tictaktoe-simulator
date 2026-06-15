import logging
from logging import Logger
from typing import Any

from gamesandbox.application.ports.logger import ILogger
from gamesandbox.infrastructure.domain.log import LogLevel

LOG_LEVELS_MAP: dict[LogLevel, int] = {
    LogLevel.debug: logging.DEBUG,
    LogLevel.info: logging.INFO,
    LogLevel.warning: logging.WARN,
    LogLevel.error: logging.ERROR,
}


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


def create_logger(log_level: LogLevel | None) -> ILogger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(),
        ],
    )

    root = logging.getLogger()
    if log_level:
        root.setLevel(LOG_LEVELS_MAP[log_level])

    return SimpleLogger(root)
