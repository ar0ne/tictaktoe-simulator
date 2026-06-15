import random

from game.application.ports.engine import IGameEngine
from game.domain.entities import PlayerMove, GameType


class LocalRandomPlayerConnector:
    def get_next_move(self, game: IGameEngine) -> PlayerMove | None:
        # here we could get valid moves to chose from
        if game.game_type == GameType.TICTACTOE:
            return PlayerMove(game.active_player, random.choice(range(9)))
        raise ValueError(f"Unsupported game type: {game.game_type}")
