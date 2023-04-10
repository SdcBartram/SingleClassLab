class Team:

    def __init__(self, input_team_name, input_players_name, input_coach_name):
        self.name = input_team_name
        self.players = input_players_name
        self.coach = input_coach_name
        self.points = 0

    def add_player(self, input_players_name):
        self.players.append(input_players_name)

    def has_player(self, input_players_name):
        for player in self.players:
            if player == input_players_name:
                return True
        return False

    def play_game(self, input_result):
        if input_result == True:
            self.points += 3
