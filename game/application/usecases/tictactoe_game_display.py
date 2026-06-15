from game.application.ports.engine import IGameEngine
from game.application.usecases.tictactoe_game_engine import TicTacToeGameEngine, PlayerValue


class TerminalTicTacToeGameDisplay:
    """Implementation of IGameDisplay interface for TicTacToe game engine.
    Can send state of the game to the logger"""

    def display(self, game_engine: IGameEngine) -> str:
        """Print display state in stdout"""
        if not isinstance(game_engine, TicTacToeGameEngine):
            raise ValueError("Unsupported game engine to display")
        return self._get_game_info(game_engine)

    def _get_game_info(self, game_engine: TicTacToeGameEngine) -> str:
        def fmt_cell(val: PlayerValue | None) -> str:
            if val is None:
                return " "
            return val

        info = self._get_game_info_title(game_engine) + "\n"
        info += "-" * 13
        for line_idx in range(3):
            info += "\n"
            info += (
                f"| {fmt_cell(game_engine._board[line_idx * 3])} "
                f"| {fmt_cell(game_engine._board[1 + line_idx * 3])} "
                f"| {fmt_cell(game_engine._board[2 + line_idx * 3])} |\n"
            )
            info += "-" * 13
        return info

    def _get_game_info_title(self, game_engine: TicTacToeGameEngine) -> str:
        if game_engine.is_running():
            return "Game is in progress!"
        if game_engine.is_player_won(TicTacToeGameEngine.CROSS):
            return f"Cross (x) player '{game_engine._cross_player.name}' won"
        elif game_engine.is_player_won(TicTacToeGameEngine.ZERO):
            return f"Zero (o) player '{game_engine._zero_player.name}' won"
        return "Draft"
