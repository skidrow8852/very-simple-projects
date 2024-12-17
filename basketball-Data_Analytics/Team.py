class Team:
    def __init__(self, id, name, conference):
        self.id = id
        self.name = name
        self.conference = conference
        self.players = []

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_conference(self):
        return self.conference

    def get_players(self):
        return self.players

    def add_player(self, player):
        self.players.append(player)

    def has_player(self, player):
        return player in self.players

    def print_team(self):
        print(f"Team Name: {self.get_name()}, Conference: {self.get_conference()}")

    def populate_teams(team_data):
        teams = []
        for data in team_data:
            id = data[0]
            name = data[1]
            conference = data[2]
            team = Team(id, name, conference)
            teams.append(team)
        return teams
