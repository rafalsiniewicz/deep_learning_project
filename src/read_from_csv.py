import pandas as pd
def read_from_file(filename):
	#headers = {'match_results': ('Date', 'Start', 'Visitor/Neutral', 'PTS_visitor', 'Home/Neutral', 'PTS_home', '', 'Overtime', 'Attend', 'Notes')}

	df = pd.read_csv('../nba_stats/' + filename, index_col=None)
	return df

dataset = read_from_file('season_2016-17/match_results_may.csv')
print(dataset.columns)
