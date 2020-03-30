from Stats import Stats
class Player(Stats):
    def __init__(self, stats, info=dict()):
        super().__init__(stats)
        self.info = info
    
