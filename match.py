from umpire import Umpire
from commentator import Commentator

class Match:
    def __init__(self, team1, team2, field):
        self.team1 = team1
        self.team2 = team2
        self.field = field
        self.innings = 1
        self.current_batting_team = None
        self.current_bowling_team = None
        self.current_batsman = None
        self.current_bowler = None
        self.umpire = None
        self.commentator = None
        self.score_1 = 0
        self.score_2 = 0

    def start_match(self):
        if self.current_batting_team == None:
           self.current_batting_team = self.team1
        if self.current_bowling_team == None:
            self.current_bowling_team = self.team2
        self.current_batsman = self.current_batting_team.send_next_player()
        self.current_bowler = self.current_bowling_team.choose_bowler()
        self.umpire = Umpire()
        self.commentator = Commentator()

        if(self.innings == 1):
            print("Cricket Match Started!")

        for ball in range(31):
            if ball == 30:
                self.end_innings()
                break
            if self.innings == 2 and self.score_1 < self.umpire.score:
                self.end_innings()
                break
            self.umpire.overs = ball+1
            if self.current_batsman is None:
                self.end_innings()
                break
            batting_probability, bowling_probability = self.umpire.predict_outcome(self.current_batsman, self.current_bowler)
            if batting_probability > bowling_probability:
                self.umpire.handle_boundary()
                print(f"Boundary! {self.current_batsman.name} scored 4 runs.")
            else:
                self.umpire.handle_wicket()
                print(f"Wicket! {self.current_batsman.name} got out.")
                self.current_batsman = self.current_batting_team.send_next_player()
                if self.current_batsman is None or self.umpire.wickets == 10:
                    self.end_innings()
                    break

            self.commentator.provide_commentary(self.umpire)

    def end_innings(self):
        print(f"Innings {self.innings} ended.")
        if self.innings == 1:
            self.score_1 = self.umpire.score
        else:
            self.score_2 = self.umpire.score
        self.umpire.overs = 0
        self.umpire.score = 0
        self.umpire.wickets = 0
        self.innings += 1

        if self.innings > 2:
            self.end_match()
        else:
            self.current_batting_team, self.current_bowling_team = self.current_bowling_team, self.current_batting_team
            self.current_batsman = self.current_batting_team.send_next_player()
            self.current_bowler = self.current_bowling_team.choose_bowler()
            print(f"Change of Innings! {self.current_batting_team.name} is now batting.")
            self.commentator.provide_commentary(self.umpire)
            self.start_match()

    def end_match(self):
        print("Cricket Match Ended!")
        if self.score_1 > self.score_2:
            print(f"{self.team1.name} won the match!")
        elif self.score_1 < self.score_2:
            print(f"{self.team2.name} won the match!")
        else:
            print("The match ended in a tie.")