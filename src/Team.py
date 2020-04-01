from Player import *
from Game import *
class Team:
    def __init__(self, games=[], players=[], stats=pd.DataFrame()):
        super().__init__(stats)
        self.games = games  #Game
        self.players = players  #Player
    
    def get_data(self):
        pass
