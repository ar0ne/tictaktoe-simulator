import logging
from typing import Type, Sequence

from game.application.ports.player_connector import IPlayerConnector
from game.application.ports.engine import IGameEngine
from game.application.usecases.tictactoe_game_engine import TicTacToeGameEngine
from game.domain.entities import GameType, Player

logger = logging.getLogger(__name__)


class GameSimulator:
    SUPPORTED_GAMES: dict[GameType, Type[IGameEngine]] = {
        GameType.TICTACTOE: TicTacToeGameEngine,
    }

    def __init__(self, /, *, connector: IPlayerConnector, game_type: GameType, players: Sequence[Player]) -> None:
        self.connector = connector
        self.game_engine = self._create_engine(game_type, players)

    def run_simulation(self) -> None:
        logger.info("Running simulation...")
        self._init_game()
        self._simulate_game()
        logger.info("Simulation completed")

    def _create_engine(self, game_type: GameType, players: Sequence[Player]) -> IGameEngine:
        logger.debug("Create display %s for players %s", game_type, players)
        if game_type not in self.SUPPORTED_GAMES:
            raise ValueError(f"Game {game_type} is not supported")
        game = self.SUPPORTED_GAMES.get(game_type)
        if game is None:
            raise ValueError(f"Unable to initialize the display: {game_type}")
        randomized_players = list(set(players))
        return game(randomized_players)

    def _init_game(self) -> None:
        logger.info("Init the display %s", self.game_engine.game_type.name)
        self.game_engine.start()

    def _simulate_game(self) -> None:
        logger.info("Simulation in progress")
        while self.game_engine.is_running():
            if move := self.connector.get_next_move(self.game_engine):
                if self.game_engine.validate_move(move):
                    self.game_engine.apply_move(move)
