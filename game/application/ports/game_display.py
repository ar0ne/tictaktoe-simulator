from typing import Protocol

from game.application.ports.engine import IGameEngine


class IGameDisplay(Protocol):
    """
    Interface of game state display
    """
    def display(self, game: IGameEngine) -> None:
        ...
