from Stats import Stats
from Player import Player
from Game import Game
class Team:
    def __init__(self, games=[], players=[], stats=dict()):
        super().__init__(stats)
        self.games = games  #Game
        self.players = players  #Player
    
    def get_data(self):
        pass
