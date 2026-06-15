from typing import Type, Sequence

from game.application.ports.engine import IGameEngine
from game.application.ports.game_display import IGameDisplay
from game.application.ports.logger import ILogger
from game.application.ports.player_connector import IPlayerConnector
from game.application.usecases.tictactoe_game_engine import TicTacToeGameEngine
from game.domain.entities import GameType, Player


class GameSimulator:
    SUPPORTED_GAMES: dict[GameType, Type[IGameEngine]] = {
        GameType.TICTACTOE: TicTacToeGameEngine,
    }

    def __init__(self, /, *, connector: IPlayerConnector, game_type: GameType, players: Sequence[Player],
                 logger: ILogger, game_display: IGameDisplay) -> None:
        self._logger = logger
        self._connector = connector
        self._game_engine = self._create_engine(game_type, players)
        self._game_display = game_display

    def run_simulation(self) -> None:
        self._logger.info("Running simulation...")
        self._init_game()
        self._simulate_game()
        self._logger.info("Simulation completed")

    def display_state(self) -> None:
        self._game_display.display(self._game_engine)

    def _create_engine(self, game_type: GameType, players: Sequence[Player]) -> IGameEngine:
        self._logger.debug("Create display %s for players %s", game_type, players)
        if game_type not in self.SUPPORTED_GAMES:
            raise ValueError(f"Game {game_type} is not supported")
        game = self.SUPPORTED_GAMES.get(game_type)
        if game is None:
            raise ValueError(f"Unable to initialize the display: {game_type}")
        randomized_players = list(set(players))
        return game(randomized_players)

    def _init_game(self) -> None:
        self._logger.info("Initialize game: %s", self._game_engine.game_type.name)
        self._game_engine.start()

    def _simulate_game(self) -> None:
        self._logger.info("Simulation in progress")
        while self._game_engine.is_running():
            if move := self._connector.get_next_move(self._game_engine):
                if self._game_engine.validate_move(move):
                    self._game_engine.apply_move(move)
