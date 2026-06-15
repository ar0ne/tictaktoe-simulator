from game.application.ports.game_display import IGameDisplay
from game.application.ports.game_simulator import IGameSimulator
from game.application.ports.logger import ILogger
from game.application.ports.player_connector import IPlayerConnector
from game.application.usecases.game_simulator import GameSimulator
from game.application.usecases.tictactoe_game_display import TerminalTicTacToeGameDisplay
from game.domain.entities import Player, GameType, SimulationMode
from game.infrastructure.adapters.local_connector import LocalRandomPlayerConnector
from game.infrastructure.adapters.logger import create_logger
from game.infrastructure.adapters.remote_connector import RemotePlayerConnector
from game.utils.common import is_valid_url


class Container:

    def __init__(self, config: dict) -> None:
        self._config = config

    def players(self) -> list[Player]:
        p1 = Player(self._config['player1'])
        p2 = Player(self._config['player2'])
        return list({p1, p2})

    def player_connector(self) -> IPlayerConnector:
        if mode := self._config["mode"]:
            if mode == SimulationMode.REMOTE.value:
                if url := self._config["remote_url"]:
                    if not is_valid_url(url):
                        raise ValueError("remote_url is not valid URL")
                return RemotePlayerConnector(url)
            elif mode == SimulationMode.LOCAL.value:
                return LocalRandomPlayerConnector()
        raise ValueError("Mode is not valid")

    def game_type(self) -> GameType:
        return GameType.TICTACTOE

    def logger(self) -> ILogger:
        return create_logger(self._config["log_level"])

    def game_simulator(self) -> IGameSimulator:
        return GameSimulator(connector=self.player_connector(),
                             game_type=self.game_type(), players=self.players(),
                             logger=self.logger(), game_display=self.game_display())

    def game_display(self) -> IGameDisplay:
        return TerminalTicTacToeGameDisplay(self.logger())