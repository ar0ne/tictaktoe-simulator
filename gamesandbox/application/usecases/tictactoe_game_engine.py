from typing import Literal, Sequence, cast

from gamesandbox.domain.entities import Player, PlayerMove, GameType
from gamesandbox.utils.common import all_present_and_equal, all_present

type PlayerValue = Literal["x", "o"]


class TicTacToeGameEngine:
    CROSS: PlayerValue = "x"
    ZERO: PlayerValue = "o"

    _current_player: Player

    def __init__(self, players: Sequence[Player]) -> None:
        if len(players) != 2:
            raise ValueError("Should be 2 players to play the display!")
        self._board: list[PlayerValue | None] = []
        self._cross_player, self._zero_player = players

    def is_player_won(self, val: PlayerValue) -> bool:
        """
        Checks if all values are equal on any of lines.
        """
        return any((
            all_present_and_equal((self._board[0], self._board[1], self._board[2]), val),
            all_present_and_equal((self._board[3], self._board[4], self._board[5]), val),
            all_present_and_equal((self._board[6], self._board[7], self._board[8]), val),

            all_present_and_equal((self._board[0], self._board[4], self._board[8]), val),
            all_present_and_equal((self._board[2], self._board[4], self._board[6]), val),

            all_present_and_equal((self._board[0], self._board[3], self._board[6]), val),
            all_present_and_equal((self._board[1], self._board[4], self._board[7]), val),
            all_present_and_equal((self._board[2], self._board[5], self._board[8]), val),
        ))

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
        self._board[cell_idx] = self.CROSS if self._cross_player == move.player else self.ZERO
        self._toggle_active_player()

    def is_running(self) -> bool:
        """
        Checks if any player win or all cells filled.
        """
        return not any((
            self.is_player_won(self.CROSS),
            self.is_player_won(self.ZERO)
        )) and not all_present(self._board)

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
