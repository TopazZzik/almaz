class GameData:
    def __init__(self):
        self.total_count = 150
        self.count = 0
        self.players = []

    def restart(self):
        self.total_count = 150
        self.count = 0
        self.players = []

    def set_total_count(self, value):
        self.total_count = value

    def set_count(self, value):
        self.count = value

    def set_players(self, value):
        self.players = value

    def get_total_count(self):
        return self.total_count

    def get_count(self):
        return self.count

    def get_players(self):
        return self.players