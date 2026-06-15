import argparse


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="Game Simulation",
        description="Simulator of automated display rounds for TicTacToe",
    )
    parser.add_argument("player1", type=str, help="Name of Player 1")
    parser.add_argument("player2", type=str, help="Name of Player 2")
    parser.add_argument("-m", "--mode", help="Player simulation mode. Default: 'local'",
                        choices=["remote", "local"], default="local")
    parser.add_argument("-l", "--log-level", help="Logging level. Default: 'info'",
                        choices=["debug", "info", "warn", "error"], default="info")
    parser.add_argument("-r", "--remote-url", help="Uri for remote host simulation mode",
                        type=str, required=False)
    return parser