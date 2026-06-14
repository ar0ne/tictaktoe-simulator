import argparse
import logging
import sys

from game.connector import RemotePlayerConnector, LocalRandomPlayerConnector
from game.display import TerminalTicTacToeGameDisplay
from game.models import Player, GameType
from game.simulator import GameSimulator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
    ]
)

logger = logging.getLogger(__name__)


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="Game Simulation",
        description="Simulator of automated game rounds for TicTacToe",
    )
    parser.add_argument("player1", type=str, help="Name of Player 1")
    parser.add_argument("player2", type=str, help="Name of Player 2")
    parser.add_argument("-m", "--mode", help="Player simulation mode. Default: 'local'",
                        choices=["remote", "local"], default="local")
    parser.add_argument("-l", "--log-level", help="Logging level. Default: 'info'",
                        choices=["debug", "info", "warn", "error"], default="info")
    return parser


LOG_LEVELS_MAP: dict[str, int] = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warn": logging.WARN,
    "error": logging.ERROR,
}


def main(argv: list[str] | None = None) -> None:
    parser = create_parser()
    args = parser.parse_args(argv)

    logging.getLogger().setLevel(LOG_LEVELS_MAP[args.log_level])

    mode = args.mode

    if mode == "remote":
        connector = RemotePlayerConnector()
    else:
        connector = LocalRandomPlayerConnector()

    game_type = GameType.TICTACTOE
    game_display = TerminalTicTacToeGameDisplay()

    players = [Player(args.player1), Player(args.player2)]
    simulator = GameSimulator(connector=connector, game_type=game_type, players=players)
    simulator.run_simulation()
    game_display.display(simulator.game)


if __name__ == "__main__":
    main(sys.argv[1:])
