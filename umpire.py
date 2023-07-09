import random

class Umpire:
    def __init__(self):
        self.score = 0
        self.wickets = 0
        self.overs = 0

    def predict_outcome(self, batsman, bowler):
        batting_probability = batsman.batting * random.uniform(0.8, 1.2)
        bowling_probability = bowler.bowling * random.uniform(0.8, 1.2)
        return batting_probability, bowling_probability

    def handle_wicket(self):
        self.wickets += 1

    def handle_boundary(self):
        self.score += 4

    def handle_extra(self):
        self.score += 1