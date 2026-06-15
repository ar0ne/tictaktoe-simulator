import logging

import httpx

from game.application.ports.engine import IGameEngine
from game.domain.entities import PlayerMove

logger = logging.getLogger(__name__)


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
