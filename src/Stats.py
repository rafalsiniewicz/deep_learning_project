class Stats:
    def __init__(self, stats=dict()):
        self.stats = stats

    
    def get_stats(self, stat):
        return self.stats[stat]

    def show_stats(self, stat):
        print(self.stats[stat])