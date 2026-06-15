import httpx

from gamesandbox.application.ports.engine import IGameEngine
from gamesandbox.application.ports.logger import ILogger
from gamesandbox.domain.entities import PlayerMove


class RemotePlayerConnector:
    """
    Implements remote player's move connector.
    """

    def __init__(self, remote_url: str, logger: ILogger) -> None:
        self._remote_url = remote_url
        self._logger = logger

    def get_next_move(self, game: IGameEngine) -> PlayerMove | None:
        self._logger.debug("Player %s makes next move", game.active_player)
        try:
            with httpx.Client() as client:
                r = client.get(self._remote_url)
                r.raise_for_status()
                return PlayerMove(game.active_player, int(r.text))
        except httpx.HTTPError as exc:
            self._logger.warning("Unable to retrieve player's move (%s): %s", self._remote_url, exc)
            return None
