from dataclasses import dataclass

from gamesandbox.domain.entities import SimulationMode, GameType
from gamesandbox.infrastructure.domain.log import LogLevel
from gamesandbox.utils.common import is_valid_url


@dataclass
class Config:
    player1: str
    player2: str
    mode: SimulationMode
    game_type: GameType
    log_level: LogLevel
    remote_url: str | None = None

    def __post_init__(self) -> None:
        if self.mode == SimulationMode.LOCAL and self.remote_url:
            raise ValueError("remote_url is not applicable for local simulation")
        elif self.mode == SimulationMode.REMOTE and not is_valid_url(self.remote_url):
            raise ValueError("remote_url is not valid URL")
