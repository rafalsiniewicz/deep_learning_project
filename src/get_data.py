from nba_api.stats.endpoints import leaguegamefinder

gamefinder = leaguegamefinder.LeagueGameFinder(league_id_nullable='00')	# nba id is '00'
games = gamefinder.get_data_frames()[0]
print(games[['GAME_DATE']].head(5))


