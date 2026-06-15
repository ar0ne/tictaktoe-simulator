def test_display_in_progress(tictactoe_display, tictactoe):
    state = tictactoe_display.display(tictactoe)
    assert len(state) > 0
    assert "Game is in progress!" in state


def test_display_cross_win(tictactoe_display, tictactoe_bob_win):
    state = tictactoe_display.display(tictactoe_bob_win)
    assert len(state) > 0
    assert "Cross (x) player 'Bob' won" in state
    assert "| x | x | x |" in state
