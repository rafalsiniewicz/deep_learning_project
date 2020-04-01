from Game import *

stat = Game()
stat.read_from_file('season_2016-17/match_results_april.csv')
print(stat.stats)