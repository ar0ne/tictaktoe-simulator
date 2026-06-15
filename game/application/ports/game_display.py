from typing import Protocol

from game.application.ports.engine import IGameEngine


class IGameDisplay(Protocol):

    def display(self, game: IGameEngine) -> None:
        ...
