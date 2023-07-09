# Cricket Tournament Simulation

This Python program simulates a cricket tournament involving two teams. The simulation takes into account the player statistics, such as batting, bowling, fielding, running, and experience, to determine the probabilities of various events occurring during the match, such as boundaries, wickets, and runs scored.

## Methodology

The program consists of several classes:

- Player: Represents a cricket player with various statistics.
- Team: Represents a team consisting of players. Handles selecting the captain, setting the batting order, and choosing the bowler.
- Field: Represents the field conditions, including size, fan ratio, pitch conditions, and home advantage.
- Umpire: Simulates the actions of an umpire, including predicting outcomes based on player probabilities, keeping track of scores, wickets, and overs.
- Commentator: Provides live commentary during the match based on the umpire's actions and match stats.
- Match: Simulates an individual cricket match using objects of the Teams, Field, Umpire, and Commentator classes. Starts the match, handles innings, and determines the winner.

The match simulation consists of multiple balls, and each ball predicts outcomes based on the probabilities of the batsman and bowler. The umpire keeps track of the scores, wickets, and overs. The commentator provides live commentary based on the match's progress.

## Instructions

1. Install Python: Ensure that Python is installed on your system. This program is compatible with Python 3.

2. Clone the repository: Clone this repository to your local machine.

3. Navigate to the project directory: Open a terminal or command prompt and navigate to the directory where you cloned the repository.

4. Run the program: Execute the following command to run the cricket tournament simulation:

   ```shell
   python main.py
