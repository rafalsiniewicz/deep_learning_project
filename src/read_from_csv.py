import pandas as pd
def read_from_file(filename):
	df = pd.read_csv('../nba_stats/season_2018-19/' + filename)
	dataset = df.values
	return dataset

dataset = read_from_file('match_results_april.csv')
print(dataset)
