import pandas as pd
class Stats:
    def __init__(self, stats=pd.DataFrame()):
        self.stats = stats
    
    def get_stats(self, stat=''):
        try:
            return self.stats[stat]
        except:
            return self.stats

    def show_stats(self, stat):
        print(self.stats[stat])

    def read_from_file(self, filename):
        df = pd.read_csv('../nba_stats/' + filename)
        self.stats = df