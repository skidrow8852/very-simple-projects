from typing import List
from Game import Game
from Player import Player


class PlayerGameStats:
    def __init__(self, game: Game, player: Player, field_goals: int, three_points: int, free_throws: int,
                 offensive_rebounds: int, defensive_rebounds: int, assists: int):
        self.game = game
        self.player = player
        self.field_goals = field_goals
        self.three_points = three_points
        self.free_throws = free_throws
        self.offensive_rebounds = offensive_rebounds
        self.defensive_rebounds = defensive_rebounds
        self.assists = assists

    def get_player(self):
        return self.player

    def get_offensive_rebounds(self):
        return self.offensive_rebounds

    def get_defensive_rebounds(self):
        return self.defensive_rebounds

    def get_assists(self):
        return self.assists

    def get_player_game_score(self):
        return self.field_goals * 2 + self.three_points + self.free_throws

    def populate_player_game_stats(game: Game, players: List[Player], player_stats: List[List[int]]) -> List['PlayerGameStats']:
        player_game_stats_list = []

        for i in range(len(players)):
            player = players[i]
            stats = player_stats[i]
            player_stats_data = PlayerGameStats(
                game,
                player,
                stats[0],  # field_goals
                stats[1],  # three_points
                stats[2],  # free_throws
                stats[3],  # offensive_rebounds
                stats[4],  # defensive_rebounds
                stats[5]   # assists
            )
            player_game_stats_list.append(player_stats_data)

        return player_game_stats_list
