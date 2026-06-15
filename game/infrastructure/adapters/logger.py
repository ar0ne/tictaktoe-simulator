import logging

from game.application.ports.logger import ILogger
from game.application.usecases.simple_logger import SimpleLogger
from game.infrastructure.domain.log import LogLevel

LOG_LEVELS_MAP: dict[LogLevel, int] = {
    LogLevel.debug: logging.DEBUG,
    LogLevel.info: logging.INFO,
    LogLevel.warning: logging.WARN,
    LogLevel.error: logging.ERROR,
}


def create_logger(log_level: LogLevel | None) -> ILogger:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler(),
        ]
    )

    root = logging.getLogger()
    if log_level:
        root.setLevel(LOG_LEVELS_MAP[log_level])

    return SimpleLogger(root)
