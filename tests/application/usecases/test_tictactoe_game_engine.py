from functools import reduce
from typing import Sequence, Any

import pytest

from gamesandbox.domain.entities import PlayerMove, GameType


def flatten(lst: Sequence[Any]) -> list[Any]:
    return list(reduce(lambda acc, i: acc + i, lst))


def test_start(tictactoe_draft, alice, bob):
    tictactoe_draft.start()
    assert len(tictactoe_draft._board) == 9
    assert len(list(filter(lambda x: not x, tictactoe_draft._board))) == 9
    assert tictactoe_draft._cross_player == bob
    assert tictactoe_draft._zero_player == alice


def test_validate_move(tictactoe, bob):
    assert tictactoe.active_player == bob
    for idx in range(9):
        move = PlayerMove(bob, data=idx)
        assert tictactoe.validate_move(move)


def test_validate_move_invalid_data(tictactoe, alice, bob):
    assert tictactoe.active_player == bob
    for idx in range(9):
        move = PlayerMove(alice, data=idx)
        assert not tictactoe.validate_move(move)
    assert not tictactoe.validate_move(None)
    assert not tictactoe.validate_move(PlayerMove(None, 2))
    assert not tictactoe.validate_move(PlayerMove(bob, None))
    assert not tictactoe.validate_move(PlayerMove(bob, "2"))
    assert not tictactoe.validate_move(PlayerMove(bob, -1))
    assert not tictactoe.validate_move(PlayerMove(bob, 10))


def test_validate_move_occupied_cell(tictactoe, bob):
    tictactoe._board[0] = tictactoe.CROSS
    assert not tictactoe.validate_move(PlayerMove(bob, 0))


def test_apply_move(tictactoe, bob):
    assert tictactoe.active_player == bob
    tictactoe.apply_move(PlayerMove(bob, 0))
    assert not tictactoe.active_player == bob
    assert tictactoe._board[0] == tictactoe.CROSS


def test_game_type(tictactoe):
    assert tictactoe.game_type == GameType.TICTACTOE


def test_active_player(tictactoe, bob):
    assert tictactoe.active_player == bob


@pytest.mark.parametrize(
    "board, value, expected",
    (
            (
                    (
                            ("x", None, None),
                            ("o", "o", "o"),
                            ("x", None, None),
                    ),
                    "x", False
            ),
            (
                    (
                            ("x", "x", "x"),
                            ("o", None, None),
                            ("x", None, None),
                    ),
                    "x", True
            ),
            (
                    (
                            ("x", "o", "x"),
                            ("x", "x", "x"),
                            (None, None, None),
                    ),
                    "x", True
            ),
            (
                    (
                            ("x", "o", "x"),
                            (None, None, None),
                            ("x", "x", "x"),
                    ),
                    "x", True
            ),
            (
                    (
                            ("x", "o", "x"),
                            ("x", None, None),
                            ("x", None, None),
                    ),
                    "x", True
            ),
            (
                    (
                            ("x", "o", "x"),
                            (None, "o", None),
                            ("x", "o", "x"),
                    ),
                    "o", True
            ),
            (
                    (
                            ("x", "o", "o"),
                            (None, "o", "o"),
                            ("x", "x", "o"),
                    ),
                    "o", True
            ),
            (
                    (
                            ("x", "o", "o"),
                            (None, "x", "o"),
                            (None, "o", "x"),
                    ),
                    "x", True
            ),
            (
                    (
                            ("x", None, "o"),
                            (None, "o", None),
                            ("o", "x", "x"),
                    ),
                    "o", True
            ),
            (
                    (
                            ("x", None, "o"),
                            (None, "o", None),
                            ("o", "x", "x"),
                    ),
                    "x", False
            ),
    ))
def test_is_player_won(tictactoe, board, value, expected):
    tictactoe._board = flatten(board)
    print(tictactoe._board)
    assert tictactoe.is_player_won(value) == expected
