from Stats import *
class Game(Stats):
    def __init__(self, stats=pd.DataFrame(), info=dict()):
        super().__init__(stats)
        self.info = info