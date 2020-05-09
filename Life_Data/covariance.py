import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from pandas import *
import json

# set the colormap and centre the colorbar
class MidpointNormalize(colors.Normalize):
	"""
	Normalise the colorbar so that diverging bars work there way either side from a prescribed midpoint value)

	e.g. im=ax1.imshow(array, norm=MidpointNormalize(midpoint=0.,vmin=-100, vmax=100))
	"""
	def __init__(self, vmin=None, vmax=None, midpoint=None, clip=False):
		self.midpoint = midpoint
		colors.Normalize.__init__(self, vmin, vmax, clip)

	def __call__(self, value, clip=None):
		# I'm ignoring masked values and all kinds of edge cases to make a
		# simple example...
		x, y = [self.vmin, self.midpoint, self.vmax], [0, 0.5, 1]
		return np.ma.masked_array(np.interp(value, x, y), np.isnan(value))

data = json.load(open("./Life_Data/daylio.json"))

acts = []

for day in data:
    for event in data[day]:
        if(event == "monthDate" or event == "weekDay"):
            continue
        for act1 in data[day][event]['activities']:
            if(act1 not in acts):
                acts.append(act1)

acts.sort()

matrix = {}
for act1 in acts:
    matrix[act1] = {}
    for act2 in acts:
        matrix[act1][act2] = None


for day in data:
    for event in data[day]:
        if(event == "monthDate" or event == "weekDay"):
            continue
        for act1 in data[day][event]['activities']:
            for act2 in data[day][event]['activities']:
                if(matrix[act1][act2] == None):
                    matrix[act1][act2] = 1
                else:
                    matrix[act1][act2] = matrix[act1][act2] + 1

newActs = acts
diag = np.zeros(len(acts))
i = 0
for act in acts:
    diag[i] = matrix[act][act]
    i += 1

for i in range(len(acts)):
    for j in range(len(acts)-1):
        if(diag[j] < diag[j+1]):
            temp = diag[j]
            diag[j] = diag[j+1]
            diag[j+1] = temp
            temp = newActs[j]
            newActs[j] = newActs[j+1]
            newActs[j+1] = temp

print("DIAG VALUES")
print(diag)

df = DataFrame(matrix).transpose()
df = df.reindex(columns=newActs)
df = df.reindex(newActs)
print(df)


plt.imshow(df, cmap='jet', norm=MidpointNormalize(midpoint=5,vmin=1, vmax=35))
#plt.pcolor(df, cmap='hsv', vmin=0)
plt.colorbar()
plt.yticks(np.arange(0, len(df.index), 1), df.index)
plt.xticks(np.arange(0, len(df.columns), 1), df.columns, rotation=90)

# Minor ticks
ax = plt.gca()
ax.set_yticks(np.arange(-.5, len(df.index), 1), minor=True)
ax.set_xticks(np.arange(-.5, len(df.columns), 1), minor=True)
# Gridlines based on minor ticks
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
plt.show()