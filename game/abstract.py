from abc import ABC

from game.models import PlayerMove, Player, GameType


class GameEngine(ABC):

    def start(self) -> None:
        ...

    def validate_move(self, move: PlayerMove) -> bool:
        ...

    def apply_move(self, move: PlayerMove) -> None:
        ...

    def is_running(self) -> bool:
        ...

    def get_active_player(self) -> Player:
        ...

    def get_game_info(self) -> str:
        ...

    def get_game_type(self) -> GameType:
        ...
