from typing import Type

from gamesandbox.application.ports.engine import IGameEngine
from gamesandbox.application.ports.game_display import IGameDisplay
from gamesandbox.application.ports.game_simulator import IGameSimulator
from gamesandbox.application.ports.logger import ILogger
from gamesandbox.application.ports.player_connector import IPlayerConnector
from gamesandbox.application.usecases.game_simulator import GameSimulator
from gamesandbox.application.usecases.tictactoe_game_display import (
    TerminalTicTacToeGameDisplay,
)
from gamesandbox.application.usecases.tictactoe_game_engine import TicTacToeGameEngine
from gamesandbox.domain.entities import Player, GameType, SimulationMode
from gamesandbox.infrastructure.adapters.local_connector import (
    LocalRandomPlayerConnector,
)
from gamesandbox.infrastructure.adapters.logger import create_logger
from gamesandbox.infrastructure.adapters.remote_connector import RemotePlayerConnector
from gamesandbox.infrastructure.domain.config import Config

SUPPORTED_GAMES: dict[GameType, Type[IGameEngine]] = {
    GameType.TICTACTOE: TicTacToeGameEngine,
}


class Container:
    def __init__(self, config: Config) -> None:
        self._config = config

    def players(self) -> list[Player]:
        p1 = Player(self._config.player1)
        p2 = Player(self._config.player2)
        return list({p1, p2})

    def player_connector(self) -> IPlayerConnector:
        logger = self.logger()
        if self._config.mode == SimulationMode.REMOTE and self._config.remote_url:
            return RemotePlayerConnector(self._config.remote_url, logger)
        return LocalRandomPlayerConnector(logger)

    def logger(self) -> ILogger:
        return create_logger(self._config.log_level)

    def game_simulator(self) -> IGameSimulator:
        return GameSimulator(
            connector=self.player_connector(),
            game_engine=self.game_engine(),
            logger=self.logger(),
            game_display=self.game_display(),
        )

    def game_engine(self) -> IGameEngine:
        if (game_type := self._config.game_type) not in SUPPORTED_GAMES:
            raise ValueError(f"Unsupported game type: {self._config.game_type}")
        return SUPPORTED_GAMES[game_type](self.players())

    def game_display(self) -> IGameDisplay:
        return TerminalTicTacToeGameDisplay()
