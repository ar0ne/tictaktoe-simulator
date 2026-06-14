"""
CLI
parse args
internal random generator
remote random generator
=> send valid moves and generator chose random

start game
check game state
repeat until game over
show final result


Player

Game (protocol)
    turn

TikTacToe (implementation)
    turn

PlayerInput
    Local
    Remote
    ...

"""
from abc import ABC
from typing import Protocol

from utils import all_present_and_equal


class Player:
    ...

class Game(ABC):
    def __init__(self, players: list[Player]) -> None:
        self.players = players

    def start(self) -> None:
        ...

    def next_turn(self) -> None:
        ...


class TicTacToe(Game):
    CROSS = True
    ZERO = False

    def __init__(self, players: list[Player]) -> None:
        super().__init__(players)
        self.board: list[bool | None] = []

    def start(self) -> None:
        self.board = [None for _ in range(9)]
        # cross should make first turn

    @property
    def is_game_finished(self) -> bool:
        """
        0, 1, 2
        3, 4, 5
        6, 7, 8
        """
        return any((
            all_present_and_equal((self.board[0], self.board[1], self.board[2])),
            all_present_and_equal((self.board[3], self.board[4], self.board[5])),
            all_present_and_equal((self.board[6], self.board[7], self.board[8])),

            all_present_and_equal((self.board[0], self.board[4], self.board[8])),
            all_present_and_equal((self.board[2], self.board[4], self.board[6])),

            all_present_and_equal((self.board[0], self.board[3], self.board[6])),
            all_present_and_equal((self.board[1], self.board[4], self.board[7])),
            all_present_and_equal((self.board[2], self.board[5], self.board[8])),
        ))

    @property
    def active_player(self) -> Player:
        return None

    def next_turn(self) -> None:
        while not self.is_game_finished:
            cur_player = self.active_player
            # turn = get_next_move(cur_player)
            # self.validate_move(cur_player, turn)
            # self.save_move(cur_player, turn)
        # self.show_game_result()