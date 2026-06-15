import sys

from game.infrastructure.adapters.cli import create_parser, read_config
from game.infrastructure.di import Container


def main(argv: list[str] | None = None) -> None:
    parser = create_parser()
    config = read_config(argv, parser)

    container = Container(config)
    simulator = container.game_simulator()
    simulator.run_simulation()
    simulator.display_state()


if __name__ == "__main__":
    main(sys.argv[1:])
