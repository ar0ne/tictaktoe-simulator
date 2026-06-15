from typing import Literal, Sequence, cast

from gamesandbox.domain.entities import Player, PlayerMove, GameType
from gamesandbox.utils.common import all_present_and_equal, all_present

type PlayerValue = Literal["x", "o"]


class TicTacToeGameEngine:
    CROSS: PlayerValue = "x"
    ZERO: PlayerValue = "o"

    WIN_INDEXES = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 4, 8),
        (2, 4, 6),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
    )

    _current_player: Player

    def __init__(self, players: Sequence[Player]) -> None:
        if len(players) != 2:
            raise ValueError("Should be 2 players to play the display!")
        self._board: list[PlayerValue | None] = []
        self._cross_player, self._zero_player = players

    def is_player_won(self, value: PlayerValue) -> bool:
        """
        Checks if all values are equal on any of win lines.
        """

        def get_line_values(indexes: Sequence[int]) -> list[PlayerValue | None]:
            return [self._board[idx] for idx in indexes]

        return any(
            (
                all_present_and_equal(get_line_values(line_idx), value)
                for line_idx in self.WIN_INDEXES
            )
        )

    def start(self) -> None:
        """
        Init new display round.
        """
        self._board = [None for _ in range(9)]
        self._current_player = self._cross_player

    def validate_move(self, move: PlayerMove) -> bool:
        """
        Validates if display turn is allowed
        """
        if move is None or move.player is None or move.data is None:
            return False
        if move.player is not self.active_player:
            return False
        if not isinstance(move.data, int):
            return False
        cell_idx: int = move.data
        if 0 < cell_idx > 8:
            return False
        if self._board[cell_idx] is not None:
            return False
        return True

    def apply_move(self, move: PlayerMove) -> None:
        """Applies display move"""
        cell_idx: int = cast(int, move.data)
        self._board[cell_idx] = (
            self.CROSS if self._cross_player == move.player else self.ZERO
        )
        self._toggle_active_player()

    def is_running(self) -> bool:
        """
        Checks if any player win or all cells filled.
        """
        return not any(
            (self.is_player_won(self.CROSS), self.is_player_won(self.ZERO))
        ) and not all_present(self._board)

    def _toggle_active_player(self) -> None:
        self._current_player = (
            self._zero_player
            if self.active_player == self._cross_player
            else self._cross_player
        )

    @property
    def active_player(self) -> Player:
        return self._current_player

    @property
    def game_type(self) -> GameType:
        return GameType.TICTACTOE
