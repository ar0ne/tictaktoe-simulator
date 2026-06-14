import enum
from dataclasses import dataclass
from typing import Any


class GameType(enum.Enum):
    TICTACTOE = enum.auto()


@dataclass
class Player:
    name: str

    def __hash__(self) -> int:
        return hash(self.name)


@dataclass
class PlayerMove:
    player: Player
    data: Any
