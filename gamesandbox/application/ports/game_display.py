from typing import Protocol

from gamesandbox.application.ports.engine import IGameEngine


class IGameDisplay(Protocol):
    """
    Interface of gamesandbox state display
    """

    def display(self, game_engine: IGameEngine) -> str:
        ...
