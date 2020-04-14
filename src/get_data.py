from nba_api.stats.endpoints import leaguegamefinder
from os import path, mkdir
import pandas as pd

PATH = ("../data/")
FILENAME = "games.csv"

def main():
    gamefinder = leaguegamefinder.LeagueGameFinder(league_id_nullable='00')	# nba id is '00'
    games = gamefinder.get_data_frames()[0]
    if not os.path.exists(PATH):
        os.mkdir(PATH)
    if not os.path.exists(os.path.join(PATH, FILENAME)):
        with open(os.path.join(PATH, FILENAME), 'w') as fp: 
            pass
    games.to_csv(os.path.join(PATH, FILENAME))


if __name__ == "__main__"
    main()



