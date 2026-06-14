import random
from typing import Protocol

from game.abstract import GameEngine
from game.models import PlayerMove, GameType


class PlayerConnector(Protocol):

    def get_next_move(self, game: GameEngine) -> PlayerMove:
        ...


class LocalRandomPlayerConnector:
    def get_next_move(self, game: GameEngine) -> PlayerMove:
        # here we could get valid moves to chose from
        if game.get_game_type() == GameType.TICTACTOE:
            return PlayerMove(game.get_active_player(), random.choice(range(9)))
        raise ValueError(f"Unsupported game type: {game.get_game_type()}")


class RemotePlayerConnector:
    def get_next_move(self, game: GameEngine) -> PlayerMove:
        ...
