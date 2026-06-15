import random

from game.application.ports.engine import IGameEngine
from game.application.ports.logger import ILogger
from game.domain.entities import PlayerMove, GameType


class LocalRandomPlayerConnector:
    """
    Implements random player's move connection.
    """

    def __init__(self, logger: ILogger) -> None:
        self._logger = logger

    def get_next_move(self, game: IGameEngine) -> PlayerMove | None:
        self._logger.debug("Player %s makes next move", game.active_player)
        # here we could get valid moves to chose from
        if game.game_type == GameType.TICTACTOE:
            return PlayerMove(game.active_player, random.choice(range(9)))
        raise ValueError(f"Unsupported game type: {game.game_type}")
