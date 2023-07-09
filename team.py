import random

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batting_order = []

    def select_captain(self, captain):
        self.captain = captain

    def set_batting_order(self, batting_order):
        self.batting_order = batting_order

    def send_next_player(self):
        if self.batting_order:
            return self.batting_order.pop(0)
        return None

    def choose_bowler(self):
        return random.choice(self.players)