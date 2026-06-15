from gamesandbox.application.ports.engine import IGameEngine
from gamesandbox.application.ports.game_display import IGameDisplay
from gamesandbox.application.ports.logger import ILogger
from gamesandbox.application.ports.player_connector import IPlayerConnector


class GameSimulator:
    def __init__(
        self,
        /,
        *,
        connector: IPlayerConnector,
        game_engine: IGameEngine,
        logger: ILogger,
        game_display: IGameDisplay,
    ) -> None:
        self._logger = logger
        self._connector = connector
        self._game_engine = game_engine
        self._game_display = game_display

    def run_simulation(self) -> None:
        self._logger.info("Running simulation...")
        self._init_game()
        self._simulate_game()
        self._logger.info("Simulation completed")

    def display_state(self) -> None:
        state = self._game_display.display(self._game_engine)
        self._logger.info(state)

    def _init_game(self) -> None:
        self._logger.info(
            "Initialize gamesandbox: %s", self._game_engine.game_type.name
        )
        self._game_engine.start()

    def _simulate_game(self) -> None:
        self._logger.info("Simulation in progress")
        while self._game_engine.is_running():
            if move := self._connector.get_next_move(self._game_engine):
                if self._game_engine.validate_move(move):
                    self._game_engine.apply_move(move)
