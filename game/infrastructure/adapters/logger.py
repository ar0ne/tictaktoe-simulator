import logging

from game.application.ports.logger import ILogger
from game.application.usecases.simple_logger import SimpleLogger

LOG_LEVELS_MAP: dict[str, int] = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warn": logging.WARN,
    "error": logging.ERROR,
}


def create_logger(log_level: str | None) -> ILogger:
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
