from typing import Sequence

from mypy.semanal_shared import Protocol

from game.domain.entities import PlayerMove, Player, GameType


class IGameEngine(Protocol):

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

    @property
    def active_player(self) -> Player:
        ...

    @property
    def game_type(self) -> GameType:
        ...
