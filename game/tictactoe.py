import logging
import random
from typing import Literal, Sequence, cast

from game.models import Player, PlayerMove, GameType
from game.utils import all_present_and_equal, all_present

type PlayerValue = Literal["x", "o"]

logger = logging.getLogger(__name__)


class TicTacToe:
    CROSS: PlayerValue = "x"
    ZERO: PlayerValue = "o"

    current_player: Player

    def __init__(self, players: Sequence[Player]) -> None:
        if len(players) != 2:
            raise ValueError("Should be 2 players to play the game!")
        self.board: list[PlayerValue | None] = []
        self.cross_player = players[0]
        self.zero_player = players[1]

    def is_player_won(self, player_value: PlayerValue) -> bool:
        """
        Checks if all values are equal on any of lines.
        """
        return any((
            all_present_and_equal((self.board[0], self.board[1], self.board[2]), player_value),
            all_present_and_equal((self.board[3], self.board[4], self.board[5]), player_value),
            all_present_and_equal((self.board[6], self.board[7], self.board[8]), player_value),

            all_present_and_equal((self.board[0], self.board[4], self.board[8]), player_value),
            all_present_and_equal((self.board[2], self.board[4], self.board[6]), player_value),

            all_present_and_equal((self.board[0], self.board[3], self.board[6]), player_value),
            all_present_and_equal((self.board[1], self.board[4], self.board[7]), player_value),
            all_present_and_equal((self.board[2], self.board[5], self.board[8]), player_value),
        ))

    def start(self) -> None:
        """
        Init new game round.
        """
        logger.debug("Initialize TicTacToe game engine")
        self.board = [None for _ in range(9)]
        self.current_player = random.choice((self.cross_player, self.zero_player))

    def validate_move(self, move: PlayerMove) -> bool:
        """Validates if game turn is allowed"""
        if move is None or move.player is None or move.data is None:
            return False
        if move.player is not self.active_player:
            return False
        if not isinstance(move.data, int):
            return False
        cell_idx: int = move.data
        if 0 < cell_idx > 8:
            return False
        if self.board[cell_idx] is not None:
            return False
        return True

    def apply_move(self, move: PlayerMove) -> None:
        """Applies game move"""
        logger.debug("Applying game move %s", move)
        cell_idx: int = cast(int, move.data)
        self.board[cell_idx] = self.CROSS if self.cross_player == move.player else self.ZERO
        self._toggle_active_player()

    def is_running(self) -> bool:
        """
        Checks if any player win or all cells filled.
        """
        return not any((
            self.is_player_won(self.CROSS),
            self.is_player_won(self.ZERO)
        )) and not all_present(self.board)

    def _toggle_active_player(self) -> None:
        self.current_player = (
            self.zero_player
            if self.active_player == self.cross_player
            else self.cross_player
        )

    @property
    def active_player(self) -> Player:
        return self.current_player

    @property
    def game_type(self) -> GameType:
        return GameType.TICTACTOE
