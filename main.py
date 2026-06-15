import sys
from argparse import ArgumentParser

from game.domain.entities import SimulationMode
from game.infrastructure.adapters.cli import create_parser
from game.infrastructure.di import Container
from game.infrastructure.domain.config import Config, LogLevel


def read_config(argv: list[str] | None, parser: ArgumentParser) -> Config:
    args = parser.parse_args(argv)

    config = Config(
        player1=args.player1,
        player2=args.player2,
        mode=SimulationMode(args.mode),
        log_level=LogLevel(args.log_level),
        remote_url=args.remote_url,
    )
    return config


def main(argv: list[str] | None = None) -> None:
    parser = create_parser()
    config = read_config(argv, parser)

    container = Container(config)
    simulator = container.game_simulator()
    simulator.run_simulation()
    simulator.display_state()


if __name__ == "__main__":
    main(sys.argv[1:])
