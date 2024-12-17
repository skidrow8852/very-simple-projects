from typing import List, Dict

from Player import Player
from Team import Team

class Game:
    def __init__(self, game_number: int, date: str, home_team: Team, away_team: Team, attendance: int):
        self.game_number = game_number
        self.date = date
        self.home_team = home_team
        self.away_team = away_team
        self.attendance = attendance
        self.player_game_stats = []
        self.home_team_score = 0
        self.away_team_score = 0
        self.winner = None

    # Getters
    def get_home_team(self):
        return self.home_team

    def get_away_team(self):
        return self.away_team
    
    def get_game_number(self):
        return self.game_number

    # Method to add player game stats
    def add_player_game_stats(self, stats):
        self.player_game_stats.append(stats)

    # Method to get player game stats
    def get_player_game_stats(self):
        return self.player_game_stats

    # Static method to populate games
    def populate_games(teams: List, game_data: List[List[str]]) -> List:
        games = []
        for data in game_data:
            game_number = int(data[0])  # Game number
            date = data[1]  # Game date
            home_team = teams[int(data[2])]  # Get home team
            away_team = teams[int(data[3])]  # Get away team
            attendance = int(data[4])  # Attendance
            # Create and add game to list
            game = Game(game_number, date, home_team, away_team, attendance)
            games.append(game)
        return games

    # Function to get sum of the PlayerGameScore for each player 
    # in the game to compute the team score 
    def teams_score(self):
        self.home_team_score = self.calculate_team_score(self.home_team)
        self.away_team_score = self.calculate_team_score(self.away_team)
        if self.home_team_score > self.away_team_score:
            print(f"Team {self.home_team.get_name()} score: {self.home_team_score}")
            print(f"Team {self.away_team.get_name()} score: {self.away_team_score}")
        else:
            print(f"Team {self.away_team.get_name()} score: {self.away_team_score}")
            print(f"Team {self.home_team.get_name()} score: {self.home_team_score}")

    # Helper function to get game score
    def calculate_team_score(self, team) -> int:
        team_score = 0
        for stats in self.player_game_stats:
            player = stats.get_player()
            if team.has_player(player):
                team_score += stats.get_player_game_score()
        return team_score

    # Function to get game summary
    def game_summary(self) -> str:
        self.teams_score()
        if self.home_team_score > self.away_team_score:
            self.winner = self.home_team
            return f"{self.home_team.get_name()} wins against {self.away_team.get_name()} with a score of {self.home_team_score} - {self.away_team_score}"
        elif self.home_team_score < self.away_team_score:
            self.winner = self.away_team
            return f"{self.away_team.get_name()} wins against {self.home_team.get_name()} with a score of {self.away_team_score} - {self.home_team_score}"
        else:
            self.winner = None
            return f"The game between {self.home_team.get_name()} and {self.away_team.get_name()} ended in a draw with a score of {self.home_team_score} - {self.away_team_score}"

    # Function to get highest team scorer
    def highest_team_scorer(self, team) -> 'Player':
        highest_scorer = None
        highest_score = float('-inf')
        for stats in self.player_game_stats:
            player = stats.get_player()
            if team.has_player(player):
                player_score = stats.get_player_game_score()
                if player_score > highest_score:
                    highest_score = player_score
                    highest_scorer = player
        return highest_scorer

    # Helper function to get highest scorers in a game
    def highest_scorer(self) -> Dict:
        highest_scorers = {}

        home_team_scorer = self.highest_team_scorer(self.home_team)
        away_team_scorer = self.highest_team_scorer(self.away_team)

        highest_scorers[self.home_team] = home_team_scorer
        highest_scorers[self.away_team] = away_team_scorer

        return highest_scorers
    
    def get_winning_team(self):
        if self.home_team_score > self.away_team_score:
            return self.home_team
        elif self.away_team_score > self.home_team_score:
            return self.away_team
        else:
            return None  # Draw
