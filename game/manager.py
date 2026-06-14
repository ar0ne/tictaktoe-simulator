from typing import Type

from game.abstract import GameEngine
from game.connectors import PlayerConnector
from game.models import GameType, Player, PlayerMove
from game.tictactoe import TicTacToe


class GameManager:
    SUPPORTED_GAMES: dict[GameType, Type[GameEngine]] = {
        GameType.TICTACTOE: TicTacToe,
    }

    def __init__(self, player_connector: PlayerConnector) -> None:
        self.connector = player_connector

    def create_game(self, game_type: GameType, players: list[Player]) -> GameEngine:
        if game_type not in self.SUPPORTED_GAMES:
            raise ValueError(f"Game {game_type} is not supported")
        game = self.SUPPORTED_GAMES.get(game_type)
        randomized_players = list(set(players))
        return game(randomized_players)

    def play(self, game: GameEngine) -> None:
        while game.is_running():
            move = self.get_next_player_move(game)
            if game.validate_move(move):
                game.apply_move(move)

    def display_results(self, game: GameEngine) -> None:
        print(game.get_game_info())

    def get_next_player_move(self, game: GameEngine) -> PlayerMove:
        # request move from Player
        return self.connector.get_next_move(game)
