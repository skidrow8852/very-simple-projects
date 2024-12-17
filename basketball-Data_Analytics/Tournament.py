from collections import defaultdict, OrderedDict

class Tournament:
    def __init__(self, name, season):
        self.name = name
        self.season = season
        self.teams = []
        self.games = []
        self.mvp = None

    # Getters and setters
    def add_team(self, team):
        self.teams.append(team)

    def get_teams(self):
        return self.teams

    def get_name(self):
        return self.name

    def add_game(self, game):
        self.games.append(game)

    def get_games(self):
        return self.games

    def set_mvp(self, player):
        self.mvp = player

    # Method to get the highest scorer of the tournament
    def highest_scorer(self, games):
        player_scores = defaultdict(int)

        # Aggregate scores for all players
        for game in games:
            for stats in game.get_player_game_stats():
                player = stats.get_player()
                player_score = stats.get_player_game_score()
                player_scores[player] += player_score

        # Check if the player_scores dictionary is empty
        if not player_scores:
            return None

        # Find the player with the highest score
        highest_scorer = max(player_scores, key=player_scores.get)
        self.set_mvp(highest_scorer)
        return highest_scorer

    # Method to get MVP stats
    def mvp_stats(self, games):
        stats = OrderedDict()
        total_games_played = 0
        total_points_scored = 0
        total_rebounds = 0
        total_assists = 0
        player_name = ""

        for game in games:
            for game_stats in game.get_player_game_stats():
                player = game_stats.get_player()
                if player == self.mvp:
                    total_games_played += 1
                    total_points_scored += game_stats.get_player_game_score()
                    total_rebounds += game_stats.get_offensive_rebounds() + game_stats.get_defensive_rebounds()
                    total_assists += game_stats.get_assists()
                    player_name = player.get_name()

        print("-------------------------------------------------------")
        stats["MVP Player"] = player_name
        stats["Total Rebounds"] = str(total_rebounds)
        stats["Total Assists"] = str(total_assists)
        stats["Total Games Played"] = str(total_games_played)
        stats["Total Points Scored"] = str(total_points_scored)

        return stats

    # Method to get the tournament winner team
    def get_tournament_winner(self):
        # Create a map to count wins for each team
        team_wins = defaultdict(int)

        # Iterate over games to count wins
        for game in self.games:
            winning_team = game.get_winning_team()
            if winning_team:
                team_wins[winning_team] += 1

        # Find the team with the most wins
        potential_winner = None
        max_wins = 0
        draw = False

        for team, wins in team_wins.items():
            if wins > max_wins:
                max_wins = wins
                potential_winner = team
                draw = False  # reset the draw flag
            elif wins == max_wins:
                draw = True  # if multiple teams have the same max_wins

        # If there's a draw, no clear winner, return None or some indication of a draw
        if draw:
            return None  # Represents a draw

        return potential_winner  # Returns the team with the most wins if no draw
