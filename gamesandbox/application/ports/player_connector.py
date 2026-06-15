from typing import Protocol

from gamesandbox.application.ports.engine import IGameEngine
from gamesandbox.domain.entities import PlayerMove


class IPlayerConnector(Protocol):

    def get_next_move(self, game: IGameEngine) -> PlayerMove | None:
        ...
