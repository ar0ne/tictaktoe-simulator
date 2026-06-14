import logging
from typing import Type, Protocol, Sequence

from game.connector import IPlayerConnector
from game.engine import IGameEngine
from game.models import GameType, Player, PlayerMove
from game.tictactoe import TicTacToe

logger = logging.getLogger(__name__)


class IGameController(Protocol):
    """Interface of controller that works with game engines"""
    def __init__(self, connector: IPlayerConnector) -> None:
        ...

    def create_engine(self, game_type: GameType, players: Sequence[Player]) -> IGameEngine:
        ...

    def start(self, game: IGameEngine) -> None:
        ...

    def play(self, game: IGameEngine) -> None:
        ...

    def display_game_results(self, game: IGameEngine) -> None:
        ...

    def get_next_player_move(self, game: IGameEngine) -> PlayerMove:
        ...


class GameManager:
    SUPPORTED_GAMES: dict[GameType, Type[IGameEngine]] = {
        GameType.TICTACTOE: TicTacToe,
    }

    def __init__(self, connector: IPlayerConnector) -> None:
        self.connector = connector

    def create_engine(self, game_type: GameType, players: Sequence[Player]) -> IGameEngine:
        logger.debug("Create game %s for players %s", game_type, players)
        if game_type not in self.SUPPORTED_GAMES:
            raise ValueError(f"Game {game_type} is not supported")
        game = self.SUPPORTED_GAMES.get(game_type)
        if game is None:
            raise ValueError(f"Unable to initialize the game: {game_type}")
        randomized_players = list(set(players))
        return game(randomized_players)

    def start(self, game: IGameEngine) -> None:
        logger.info("Start the game %s", game.game_type)
        game.start()

    def play(self, game: IGameEngine) -> None:
        while game.is_running():
            move = self.get_next_player_move(game)
            if game.validate_move(move):
                game.apply_move(move)

    def display_game_results(self, game: IGameEngine) -> None:
        logger.info(game.get_game_info())

    def get_next_player_move(self, game: IGameEngine) -> PlayerMove:
        # request move from Player
        return self.connector.get_next_move(game)
