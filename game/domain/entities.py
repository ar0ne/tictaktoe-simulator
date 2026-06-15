import enum
from dataclasses import dataclass
from typing import Any


class GameType(enum.Enum):
    TICTACTOE = enum.auto()


class SimulationMode(enum.Enum):
    REMOTE = "remote"
    LOCAL = "local"


@dataclass
class Player:
    name: str

    def __hash__(self) -> int:
        return hash(self.name)


@dataclass
class PlayerMove:
    player: Player
    data: Any
