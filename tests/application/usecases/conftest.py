import pytest

from gamesandbox.application.usecases.tictactoe_game_display import (
    TerminalTicTacToeGameDisplay,
)
from gamesandbox.application.usecases.tictactoe_game_engine import TicTacToeGameEngine
from gamesandbox.domain.entities import Player


@pytest.fixture
def bob():
    return Player("Bob")


@pytest.fixture
def alice():
    return Player("Alice")


@pytest.fixture
def players(bob, alice):
    return [bob, alice]


@pytest.fixture
def tictactoe_draft(players):
    return TicTacToeGameEngine(players)


@pytest.fixture
def tictactoe(tictactoe_draft):
    tictactoe_draft.start()
    return tictactoe_draft


@pytest.fixture
def tictactoe_display():
    return TerminalTicTacToeGameDisplay()


@pytest.fixture
def tictactoe_bob_win(tictactoe, bob):
    tictactoe._board = ["x", "x", "x", None, None, None, None, None, None]
    tictactoe._current_player = tictactoe._cross_player = bob
    return tictactoe
