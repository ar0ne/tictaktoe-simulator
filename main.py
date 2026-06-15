import sys

from game.infrastructure.adapters.cli import create_parser
from game.infrastructure.di import Container


def main(argv: list[str] | None = None) -> None:
    parser = create_parser()
    args = parser.parse_args(argv)

    config = {
        "player1": args.player1,
        "player2": args.player2,
        "mode": args.mode,
        "remote_url": args.remote_url,
        "log_level": args.log_level
    }

    container = Container(config)
    simulator = container.game_simulator()
    simulator.run_simulation()
    simulator.display_state()

if __name__ == "__main__":
    main(sys.argv[1:])
