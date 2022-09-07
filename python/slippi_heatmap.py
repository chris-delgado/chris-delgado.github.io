import os, math, json, glob, time, cv2, numpy as np, pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from characters import CHARACTERS
from matplotlib.offsetbox import OffsetImage,AnnotationBbox

directory = '/Users/christopherdelgado/Documents/Geany_Scripts/slippistats/'
os.chdir(directory)
df = pd.read_json('slippi_files/SlippiStats.json')

# Win Rate Per Matchup
wins_per_mu = df[df['Result'] == 'W'].groupby(['My_Character', 'Opponent_Character'])['Result'].count()
no_nc = df[['My_Character', 'Opponent_Character', 'Result']].where(df['Result'] != 'NC')
wins_and_losses = no_nc[no_nc.Result.notnull()]
total_games = wins_and_losses.groupby(['My_Character', 'Opponent_Character']).size()
win_rate_per_mu = (wins_per_mu /total_games).fillna(0).reset_index()

# Images
# See https://stackoverflow.com/questions/44246650/add-image-annotations-to-bar-plots
def get_charImage(name):
	path = "images/{}.png".format(name)
	im = plt.imread(path)
	return im

# Offset
def offset_image(coord, name, ax):
	img = get_charImage(name)
	im = OffsetImage(img, zoom=0.72)
	im.image.axes = ax
	ab = AnnotationBbox(im, (coord, 0),  xybox=(12, 10), frameon=False, xycoords='data',  boxcoords="offset points", pad=0)
	ab2 = AnnotationBbox(im, (0, coord),  xybox=(-10, -10), frameon=False, xycoords='data',  boxcoords="offset points", pad=0)
	ax.add_artist(ab)
	ax.add_artist(ab2)

characters = [char.name for char in CHARACTERS]

# Heatmap
placeholder = []

for my_char in CHARACTERS:
	for opp_char in CHARACTERS:
		placeholder.append(
			{
				'My_Character' : my_char.name,
				'Opponent_Character' : opp_char.name
			}
		)

empty_chart = pd.DataFrame(placeholder)
temp_df1 = pd.merge(empty_chart, win_rate_per_mu, how="outer", on=['My_Character', 'Opponent_Character']).rename(columns={0: 'Win_Rate'})
temp_df2 = pd.pivot_table(temp_df1, values="Win_Rate", index="My_Character", columns="Opponent_Character", sort=False, dropna=False)
heatmap_df = temp_df2.reindex(columns=[character.name for character in CHARACTERS])
fig, ax = plt.subplots()

sns.heatmap(heatmap_df, xticklabels=False, yticklabels=False, linewidths=1, linecolor='black', annot=True)
plt.tick_params(axis='both', which='major', labelsize=10, labelbottom=False, left=False, bottom=False, top=False, labeltop=True)
plt.xticks(rotation = 90)
ax.set_ylabel('')    
ax.set_xlabel('')

for i, c in enumerate(characters):
    offset_image(i, c, ax)

ax.set_title('Matchup Spread', y=0, pad=-14)
plt.show()
