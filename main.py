"""
CLI
parse args
remote random generator
"""
from game.connector import LocalRandomPlayerConnector
from game.manager import GameManager
from game.models import Player, GameType


def local_use_case():
    players = [Player("John"), Player("Bob")]
    manager = GameManager(connector=LocalRandomPlayerConnector())
    engine = manager.create_engine(GameType.TICTACTOE, players)
    manager.start(engine)
    manager.play(engine)
    manager.display_game_results(engine)


def main():
    local_use_case()


if __name__ == "__main__":
    main()
