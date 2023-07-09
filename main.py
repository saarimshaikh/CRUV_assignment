import random
from player import Player
from team import Team
from feild import Field
from umpire import Umpire
from commentator import Commentator
from match import Match

# Create players
player1 = Player("Sachin Tendulkar", batting=0.9, bowling=0.2, fielding=0.9, running=0.8, experience=0.95)
player2 = Player("Virender Sehwag", batting=0.85, bowling=0.1, fielding=0.8, running=0.85, experience=0.9)
player3 = Player("Gautam Gambhir", batting=0.8, bowling=0.1, fielding=0.8, running=0.85, experience=0.9)
player4 = Player("Virat Kohli", batting=0.85, bowling=0.1, fielding=0.9, running=0.9, experience=0.95)
player5 = Player("Yuvraj Singh", batting=0.85, bowling=0.5, fielding=0.85, running=0.8, experience=0.9)
player6 = Player("MS Dhoni", batting=0.9, bowling=0.1, fielding=0.9, running=0.8, experience=0.95)
player7 = Player("Suresh Raina", batting=0.8, bowling=0.3, fielding=0.9, running=0.85, experience=0.9)
player8 = Player("Harbhajan Singh", batting=0.7, bowling=0.9, fielding=0.8, running=0.8, experience=0.9)
player9 = Player("Zaheer Khan", batting=0.6, bowling=0.9, fielding=0.85, running=0.8, experience=0.95)
player10 = Player("Munaf Patel", batting=0.4, bowling=0.8, fielding=0.8, running=0.75, experience=0.9)
player11 = Player("Ashish Nehra", batting=0.3, bowling=0.9, fielding=0.75, running=0.7, experience=0.9)

player12 = Player("Shane Watson", batting=0.85, bowling=0.8, fielding=0.9, running=0.85, experience=0.95)
player13 = Player("Brad Haddin", batting=0.75, bowling=0.1, fielding=0.9, running=0.8, experience=0.9)
player14 = Player("Ricky Ponting", batting=0.9, bowling=0.2, fielding=0.9, running=0.8, experience=0.95)
player15 = Player("Michael Clarke", batting=0.85, bowling=0.3, fielding=0.9, running=0.85, experience=0.9)
player16 = Player("Cameron White", batting=0.8, bowling=0.4, fielding=0.85, running=0.8, experience=0.9)
player17 = Player("Michael Hussey", batting=0.9, bowling=0.2, fielding=0.9, running=0.85, experience=0.95)
player18 = Player("David Hussey", batting=0.8, bowling=0.3, fielding=0.9, running=0.8, experience=0.9)
player19 = Player("Mitchell Johnson", batting=0.6, bowling=0.9, fielding=0.8, running=0.75, experience=0.9)
player20 = Player("Brett Lee", batting=0.6, bowling=0.9, fielding=0.8, running=0.75, experience=0.95)
player21 = Player("Shaun Tait", batting=0.4, bowling=0.9, fielding=0.8, running=0.75, experience=0.9)
player22 = Player("Jason Krejza", batting=0.2, bowling=0.8, fielding=0.8, running=0.7, experience=0.9)

# Create teams
team1 = Team("India", [player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11])
team2 = Team("Australia", [player12, player13, player14, player15, player16, player17, player18, player19, player20, player21, player22])

# Set captain and batting order
team1.select_captain(player6)
team1.set_batting_order([player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11])

team2.select_captain(player12)
team2.set_batting_order([player12, player13, player14, player15, player16, player17, player18, player19, player20, player21, player22])

# Create field
field = Field(size="medium", fan_ratio=0.8, pitch_conditions="dry", home_advantage=0.1)

# Create match
match = Match(team1, team2, field)

# Start the match
match.start_match()




