from typing import Sequence

from mypy.semanal_shared import Protocol

from game.models import PlayerMove, Player, GameType


class IGameEngine(Protocol):

    @property
    def active_player(self) -> Player:
        ...

    def __init__(self, players: Sequence[Player]) -> None:
        ...

    def start(self) -> None:
        ...

    def validate_move(self, move: PlayerMove) -> bool:
        ...

    def apply_move(self, move: PlayerMove) -> None:
        ...

    def is_running(self) -> bool:
        ...

    def get_game_info(self) -> str:
        ...

    def get_game_type(self) -> GameType:
        ...
