import logging
import random
from typing import Protocol

import httpx

from game.engine import IGameEngine
from game.models import PlayerMove, GameType

logger = logging.getLogger(__name__)


class IPlayerConnector(Protocol):

    def get_next_move(self, game: IGameEngine) -> PlayerMove | None:
        ...


class LocalRandomPlayerConnector:
    def get_next_move(self, game: IGameEngine) -> PlayerMove | None:
        # here we could get valid moves to chose from
        if game.game_type == GameType.TICTACTOE:
            return PlayerMove(game.active_player, random.choice(range(9)))
        raise ValueError(f"Unsupported game type: {game.game_type}")


class RemotePlayerConnector:

    def __init__(self, remote_url: str) -> None:
        self.remote_url = remote_url

    def get_next_move(self, game: IGameEngine) -> PlayerMove | None:
        try:
            with httpx.Client() as client:
                r = client.get(self.remote_url)
                r.raise_for_status()
                return PlayerMove(game.active_player, int(r.text))
        except httpx.HTTPError as exc:
            logger.warning("Unable to retrieve player's move (%s): %s", self.remote_url, exc)
