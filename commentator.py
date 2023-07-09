class Commentator:
    def __init__(self):
        pass

    def provide_commentary(self, umpire):
        print(f"Score: {umpire.score}/{umpire.wickets} - Balls: {umpire.overs}")