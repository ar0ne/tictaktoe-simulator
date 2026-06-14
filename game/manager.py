from typing import Type

from game.connectors import IPlayerConnector
from game.engine import IGameEngine
from game.models import GameType, Player, PlayerMove
from game.tictactoe import TicTacToe


class GameManager:
    MANAGED_GAMES: dict[GameType, Type[IGameEngine]] = {
        GameType.TICTACTOE: TicTacToe,
    }

    def __init__(self, connector: IPlayerConnector) -> None:
        self.connector = connector

    def create_game(self, game_type: GameType, players: list[Player]) -> IGameEngine:
        if game_type not in self.MANAGED_GAMES:
            raise ValueError(f"Game {game_type} is not supported")
        game = self.MANAGED_GAMES.get(game_type)
        if game is None:
            raise ValueError(f"Unable to initialize the game: {game_type}")
        randomized_players = list(set(players))
        return game(randomized_players)

    def play(self, game: IGameEngine) -> None:
        while game.is_running():
            move = self.get_next_player_move(game)
            if game.validate_move(move):
                game.apply_move(move)

    def display_results(self, game: IGameEngine) -> None:
        print(game.get_game_info())

    def get_next_player_move(self, game: IGameEngine) -> PlayerMove:
        # request move from Player
        return self.connector.get_next_move(game)
