from typing import Protocol

from game.application.ports.engine import IGameEngine
from game.domain.entities import PlayerMove


class IPlayerConnector(Protocol):

    def get_next_move(self, game: IGameEngine) -> PlayerMove | None:
        ...
