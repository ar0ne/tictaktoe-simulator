"""
CLI
parse args
remote random generator
"""
from game.connectors import LocalRandomPlayerConnector
from game.manager import GameManager
from game.models import Player, GameType


def local_use_case():
    players = [Player("John"), Player("Bob")]
    manager = GameManager(connector=LocalRandomPlayerConnector())
    game = manager.create_game(GameType.TICTACTOE, players)
    game.start()
    manager.play(game)
    manager.display_results(game)


def main():
    local_use_case()


if __name__ == "__main__":
    main()
