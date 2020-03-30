from Stats import Stats
class Game(Stats):
    def __init__(self, stats=dict(), info=dict()):
        super().__init__(stats)
        self.info = info