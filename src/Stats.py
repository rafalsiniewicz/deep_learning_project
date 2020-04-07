import pandas as pd
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.static import teams
class Stats:
    def __init__(self, stats=pd.DataFrame()):
        self.stats = stats
    
    def get_stats(self, stat=''):
        try:
            return self.stats[stat]
        except:
            return self.stats

    def show_stats(self, stat=''):
        try:
            print(self.stats[stat])
        except:
            print(stat, " column is not valid")

    def get_stats(self, type='', stat=''):
        '''
        function that select stats and returns DataFrame with specified stats
        args:
        -type(string): type of stats, could be: players, games, teams
        -stat(string): specified stat, e.g. rebounds, points, etc.
        returns:
        -stats(dataFrame): selected stats
        '''

        types = ['players', 'games', 'teams']
        assert type not in types, 'Invalid type'
        if type == 'players':
            pass
        elif type == 'games':
            return leaguegamefinder.LeagueGameFinder(league_id_nullable='00').get_data_frames()[0] # nba id is '00'
        elif type == 'teams':
            pass




    def read_from_file(self, filename):
        df = pd.read_csv('../nba_stats/' + filename)
        self.stats = df