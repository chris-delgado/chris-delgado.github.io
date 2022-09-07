import os, math, json, glob, time, cv2, numpy as np, pandas as pd, seaborn as sns, matplotlib.pyplot as plt
from characters import CHARACTERS

def get_charImage(name):
	path = "images/{}.png".format(name)
	im = plt.imread(path)
	return im

def offset_image(coord, name, ax):
	img = get_charImage(name)
	im = OffsetImage(img, zoom=0.72)
	im.image.axes = ax
	ab = AnnotationBbox(im, (coord, 0),  xybox=(12, 10), frameon=False, xycoords='data',  boxcoords="offset points", pad=0)
	#ab2 = AnnotationBbox(im, (0, coord),  xybox=(-10, -10), frameon=False, xycoords='data',  boxcoords="offset points", pad=0)
	ax.add_artist(ab)
	#ax.add_artist(ab2)

directory = '/Users/christopherdelgado/Documents/Geany_Scripts/slippistats/'
os.chdir(directory)
opp_counts = pd.read_json('slippi_files/SlippiStats.json')['Opponent_Tag'].value_counts()
print(opp_counts.to_string())
