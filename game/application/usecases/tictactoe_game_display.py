from game.application.ports.logger import ILogger
from game.application.usecases.tictactoe_game_engine import TicTacToeGameEngine, PlayerValue


class TerminalTicTacToeGameDisplay:
    """Implementation of IGameDisplay interface for TicTacToe game engine.
    Can send state of the game to the logger"""

    def __init__(self, logger: ILogger) -> None:
        self._logger = logger

    def display(self, game: TicTacToeGameEngine) -> None:
        """Print display state in stdout"""
        self._logger.info(self._get_game_info(game))

    def _get_game_info(self, game: TicTacToeGameEngine) -> str:
        def fmt_cell(val: PlayerValue | None) -> str:
            if val is None:
                return " "
            return val

        info = self._get_game_info_title(game) + "\n"
        info += "-" * 13
        for line_idx in range(3):
            info += "\n"
            info += (
                f"| {fmt_cell(game._board[line_idx * 3])} "
                f"| {fmt_cell(game._board[1 + line_idx * 3])} "
                f"| {fmt_cell(game._board[2 + line_idx * 3])} |\n"
            )
            info += "-" * 13
        return info

    def _get_game_info_title(self, game: TicTacToeGameEngine) -> str:
        if game.is_running():
            return "Game is in progress!"
        if game.is_player_won(TicTacToeGameEngine.CROSS):
            return f"Cross (x) player '{game._cross_player.name}' won"
        elif game.is_player_won(TicTacToeGameEngine.ZERO):
            return f"Zero (o) player '{game._zero_player.name}' won"
        return "Draft"
