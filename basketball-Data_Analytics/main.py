import csv
from typing import List
from PlayerGameStats import PlayerGameStats
from Team import Team
from Player import Player
from Game import Game
from Tournament import Tournament

class Main:

    def main():
        # Call the createTournament method to start the process
        tournament = Main.create_tournament()

        # Print tournament details
        Main.calculate_tournament_stats(tournament)

    # Create a tournament and populate its components
    def create_tournament():
        teams = Main.create_teams()
        players = Main.create_players(teams)

        # Create tournament
        tournament = Tournament("Philadelphia 76ers at Los Angeles Lakers", "2001")

        # Add teams to the tournament
        for team in teams:
            tournament.add_team(team)

        # Create games and add to tournament
        games = Main.create_games(teams, players)
        for game in games:
            tournament.add_game(game)

        return tournament
    
    # Create and populate teams
    def create_teams():
        teams = []

        # Populate teams here
        
        return teams

    # Create players and assign to teams
    def create_players(teams):
        players = []

        # Populate players here

        return players

    # Create games and add player stats
    def create_games(teams, players):
        games = []

        # Populate games and stats here

        return games

    # Method to calculate and print tournament statistics
    def calculate_tournament_stats(tournament):
        # Print tournament details
        print("\nTournament: " + tournament.get_name())
        print("-------------------------------------------------------\n")

        games = tournament.get_games()

        # Calculate and print game-wise stats
        print("---Game-wise Stats---")

        for game in games:
            print("Game # " + str(game.get_game_number()) + ":")
            print(game.game_summary())
            print("-------------------------------------------------------\n")

            # Print highest scorers for each team
            Main.print_team_highest_scorers(game)
            print("-------------------------------------------------------\n")

        # Calculate and print the tournament winner and tournament-wise stats
        Main.print_tournament_winner_and_highest_scorer(tournament, games)

        # Display MVP stats
        Main.print_mvp_stats(tournament)
        print("-------------------------------------------------------\n")

    def print_team_highest_scorers(game):
        # Get the highest scorer for each team
        team_highest_scorer = game.highest_scorer()

        # Print the highest scorer for each team
        for team, scorer in team_highest_scorer.items():
            if scorer is not None:
                print("Team: " + team.get_name() + ", Highest Scorer: " + scorer.get_name())
            else:
                print("Team: " + team.get_name() + ", Highest Scorer: None")

    # Method to print MVP stats
    def print_mvp_stats(tournament):
        # Get the MVP stats
        mvp_stats = tournament.mvp_stats(list(tournament.get_games()))

        # Print the MVP stats
        print("MVP Stats:")
        for key, value in mvp_stats.items():
            print("-- " + key + ": " + value)

    # Function to print tournament winner and highest scorer
    def print_tournament_winner_and_highest_scorer(tournament, games):
        # Get the tournament winner
        tournament_winner = tournament.get_tournament_winner()

        if tournament_winner:
            print("Tournament Winner: " + tournament_winner.get_name())
        else:
            print("The tournament ended in a draw.")

        # Get the highest scorer in the tournament
        highest_scorer = tournament.highest_scorer(games)

        if highest_scorer is not None:
            print("Highest Scorer of the Tournament: " + highest_scorer.get_name())
        else:
            print("No player scored any points in the tournament.")

if __name__ == "__main__":
    Main.main()
