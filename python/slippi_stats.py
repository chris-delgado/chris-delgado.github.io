from slippi import Game
from slippi_stats_functions import *
import os, math, json, glob, time, numpy as np, pandas as pd

# Grab Currrent Time Before Running the Code
start = time.time()
directory = '/Users/christopherdelgado/Documents/Geany_Scripts/slippistats/slippi_files/'
my_tag = "SMIL#659"

files = []
dates = []
times = []
my_chars = []
my_tags = []
opp_chars = []
opp_tags = []
stages = []
results = []
durations = []
my_l_successes = []
my_l_fails = []
my_l_rates = []
opp_l_successes = []
opp_l_fails = []
opp_l_rates = []
my_wavedashes = []
opp_wavedashes = []
my_ledgegrabs = []
opp_ledgegrabs = []
my_wavelands = []
opp_wavelands = []

os.chdir(directory)


try:
	historical = pd.read_json('SlippiStats.json') # Previously recorded games
except ValueError:
	pass

# Look through every game in the directory
for filename in glob.glob('*.slp'):

	# First check if game already in json file
	# Comment this out when adding new columns
	try:
		if historical['Filename'].str.contains(filename).any():
			continue
	except NameError:
		pass
	
	print(filename) # DEBUG
	game = Game(directory + filename)
	my_port_idx, opp_port_idx, my_char, opp_char, opp_tag = get_metadata(game, my_tag)
	result, my_l_success, my_l_fail, my_l_rate, opp_l_success, opp_l_fail, opp_l_rate, my_lg, opp_lg, my_wd, opp_wd, my_wl, opp_wl = calculate_stats(game, my_port_idx, opp_port_idx)
	
	files.append(filename)
	dates.append(game.metadata.date.strftime("%Y%m%d")) # UTC
	times.append(game.metadata.date.strftime("%H:%M:%S")) # UTC
	durations.append(math.floor(game.metadata.duration/60))
	my_chars.append(my_char)
	my_tags.append(my_tag)
	opp_chars.append(opp_char)
	opp_tags.append(opp_tag)
	stages.append(game.start.stage.name)
	results.append(result)
	my_l_successes.append(my_l_success)
	my_l_fails.append(my_l_fail)
	my_l_rates.append(my_l_rate)
	opp_l_successes.append(opp_l_success)
	opp_l_fails.append(opp_l_fail)
	opp_l_rates.append(opp_l_rate)
	my_wavedashes.append(my_wd)
	opp_wavedashes.append(opp_wd)
	my_wavelands.append(my_wl)
	opp_wavelands.append(opp_wl)
	my_ledgegrabs.append(my_lg)
	opp_ledgegrabs.append(opp_lg)

# Add values from new games to DataFrame
new_games_df = pd.DataFrame({
	'Filename' : files,
	'Date' : dates,
	'Time' : times,
	'Duration' : durations,
	'My_Character' : my_chars,
	'My_Tag' : my_tags,
	'Opponent_Character' : opp_chars,
	'Opponent_Tag' : opp_tags,
	'Stage' : stages,
	'Result' : results,
	'My_L_Success' : my_l_successes,
	'My_L_Fail' : my_l_fails,
	'My_L_Rate' : my_l_rates,
	'Opp_L_Success' : opp_l_successes,
	'Opp_L_Fail' : opp_l_fails,
	'Opp_L_Rate' : opp_l_rates,
	'My_Wavedashes' : my_wavedashes,
	'Opp_Wavedashes' : opp_wavedashes,
	'My_Wavelands' : my_wavelands,
	'Opp_Wavelands' : opp_wavelands,
	'My_Ledgegrabs' : my_ledgegrabs,
	'Opp_Ledgegrabs' : opp_ledgegrabs
}).astype(object)

# Grab Currrent Time After Running the Code
end = time.time()

#Subtract Start Time from The End Time
total_time = end - start

# Before any refactoring, takes about .25s for one file

print("\n"+ str(total_time))

# Add information from new games to existing ones
# Also reset index as historical and new_games_df both start at 0
try:
	all_games_df = pd.concat([historical, new_games_df]).reset_index(drop=True)
	print(all_games_df)
	all_games_df.to_json(r'SlippiStats.json')
except NameError:
	print(new_games_df)
	new_games_df.to_json(r'SlippiStats.json')
