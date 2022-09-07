import os, math, json, glob, time, numpy as np, pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from characters import CHARACTERS
from matplotlib.offsetbox import OffsetImage,AnnotationBbox

def get_charImage(name):
	path = "images/{}.png".format(name)
	im = plt.imread(path)
	return im

def offset_image(coord, name, ax):
	img = get_charImage(name)
	im = OffsetImage(img, zoom=0.72)
	im.image.axes = ax
	ab = AnnotationBbox(im, (0, coord),  xybox=(-10, 0), frameon=False, xycoords='data',  boxcoords="offset points", pad=0)
	ax.add_artist(ab)

directory = '/Users/christopherdelgado/Documents/Geany_Scripts/slippistats/'
os.chdir(directory)
fig, ax = plt.subplots()
chars = pd.read_json('slippi_files/SlippiStats.json')['Opponent_Character']
char_counts = chars.value_counts()
bar_chart = char_counts.sort_values(ascending=True).plot(kind='barh')
plt.xlabel("Count", labelpad=14)
plt.title("Count of Opposing Characters", y=1.02)

labels = ax.get_yticklabels()

for label in labels:
	y_pos = label.get_position()[1]
	char = label.get_text()
	offset_image(y_pos, char, ax)

plt.tick_params(left=False)
ax.tick_params(labelleft=False) 

plt.show()
