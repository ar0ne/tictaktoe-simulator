import logging
from typing import Type, Sequence

from game.connector import IPlayerConnector
from game.engine import IGameEngine
from game.models import GameType, Player, PlayerMove
from game.tictactoe import TicTacToe

logger = logging.getLogger(__name__)


class GameSimulator:
    SUPPORTED_GAMES: dict[GameType, Type[IGameEngine]] = {
        GameType.TICTACTOE: TicTacToe,
    }

    def __init__(self, /, *, connector: IPlayerConnector, game_type: GameType, players: Sequence[Player]) -> None:
        self.connector = connector
        self.game = self._create_engine(game_type, players)

    def run_simulation(self) -> None:
        logger.info("Running simulation...")
        self._init_game()
        self._simulate_game()
        logger.info("Simulation completed")

    def _create_engine(self, game_type: GameType, players: Sequence[Player]) -> IGameEngine:
        logger.debug("Create game %s for players %s", game_type, players)
        if game_type not in self.SUPPORTED_GAMES:
            raise ValueError(f"Game {game_type} is not supported")
        game = self.SUPPORTED_GAMES.get(game_type)
        if game is None:
            raise ValueError(f"Unable to initialize the game: {game_type}")
        randomized_players = list(set(players))
        return game(randomized_players)

    def _init_game(self) -> None:
        logger.info("Init the game %s", self.game.game_type.name)
        self.game.start()

    def _simulate_game(self) -> None:
        logger.info("Simulation in progress")
        while self.game.is_running():
            if move := self.connector.get_next_move(self.game):
                if self.game.validate_move(move):
                    self.game.apply_move(move)
