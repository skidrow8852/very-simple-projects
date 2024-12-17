class Player:
    
    def __init__(self, name, number):
        self.name = name
        self.number = number
    
    def get_name(self):
        return self.name

    def get_id(self):
        return self.number

    def populate_players(player_data, team_counter):
        players = []
        for data in player_data:
            team_id = int(data[0])  # Get team ID
            if team_counter == team_id:
                player = Player(data[1], int(data[2]))
                players.append(player)
        return players
