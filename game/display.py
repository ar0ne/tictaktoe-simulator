import logging
from typing import Protocol

from game.engine import IGameEngine
from game.tictactoe import TicTacToe, PlayerValue

logger = logging.getLogger(__name__)


class IGameDisplay(Protocol):

    def display(self, game: IGameEngine) -> None:
        ...


class TerminalTicTacToeGameDisplay:

    def display(self, game: TicTacToe) -> None:
        """Print game state in stdout"""
        logger.info(self._get_game_info(game))

    def _get_game_info(self, game: TicTacToe) -> str:
        def fmt_cell(val: PlayerValue | None) -> str:
            if val is None:
                return " "
            return val

        info = self._get_game_info_title(game)
        info += "\n"
        info += "-" * 13
        for line_idx in range(3):
            info += "\n"
            info += (
                f"| {fmt_cell(game.board[line_idx * 3])} "
                f"| {fmt_cell(game.board[1 + line_idx * 3])} "
                f"| {fmt_cell(game.board[2 + line_idx * 3])} |\n"
            )
            info += "-" * 13
        return info

    def _get_game_info_title(self, game: TicTacToe) -> str:
        if game.is_running():
            return "Game is in progress!"
        if game.is_player_won(TicTacToe.CROSS):
            return f"Cross (x) player '{game.cross_player.name}' won"
        elif game.is_player_won(TicTacToe.ZERO):
            return f"Zero (o) player '{game.zero_player.name}' won"
        return "Draft"