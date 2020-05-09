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

# load in data set
data = json.load(open("./Life_Data/daylio.json"))

# we need to get the complete list of activities, and the number of days in the dataset
acts = []
numDays = 0
for day in data:
    numDays+=1
    for event in data[day]:
        if(event == "monthDate" or event == "weekDay"):
            # each day in the json contains two additional contents
            # the monthDate has the day (out of 31)
            # the weekDay has the day of week ('Monday', etc)
            continue

        for act1 in data[day][event]['activities']:
            if(act1 not in acts and act1 != ''):
                acts.append(act1)

# we can sort them alphabetically (which can be nice)
# it will be resorted later so this could be removed
acts.sort()

# now we will build up our matrix of activities
matrix = {}
for act1 in acts:
    matrix[act1] = {}
    for act2 in acts:
        matrix[act1][act2] = None

# now we will loop again, but this time tracking each days activities
for day in data:
    daysActs = []
    for event in data[day]:
        if(event == "monthDate" or event == "weekDay"):
            continue
        
        for act1 in data[day][event]['activities']:
            if(act1 not in daysActs and act1 != ''):
                daysActs.append(act1)
            
    # at this point we have the list of all of the current days activitities
    # by looping though this list we can increment the intersection of all acts
    for act1 in daysActs:
        for act2 in daysActs:
            if(matrix[act1][act2] == None):
                matrix[act1][act2] = 1
            else:
                matrix[act1][act2] = matrix[act1][act2] + 1

# now we will sort the matrix by the diagonal
newActs = acts
diag = np.zeros(len(acts))
i = 0
for act in acts:
    diag[i] = matrix[act][act]
    i += 1

# Bubble sort because its a relatively small data set, and easy to code
for i in range(len(acts)):
    for j in range(len(acts)-1):
        if(diag[j] < diag[j+1]):
            temp = diag[j]
            diag[j] = diag[j+1]
            diag[j+1] = temp
            temp = newActs[j]
            newActs[j] = newActs[j+1]
            newActs[j+1] = temp

# Basic console output to ensure things were sorted correctly
print("DIAG VALUES")
print(diag)

# Build the dataframe and sort the dataframe
df = DataFrame(matrix)
df = df.reindex(columns=newActs)
df = df.reindex(newActs)
print(df)

# Setup the plot
plt.imshow(df, cmap='viridis', norm=MidpointNormalize(midpoint=10,vmin=1, vmax=30))
plt.colorbar()
plt.yticks(np.arange(0, len(df.index), 1), df.index)
plt.xticks(np.arange(0, len(df.columns), 1), df.columns, rotation=90)

# Minor ticks
ax = plt.gca()
ax.set_yticks(np.arange(-.5, len(df.index), 1), minor=True)
ax.set_xticks(np.arange(-.5, len(df.columns), 1), minor=True)
# Gridlines based on minor ticks
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)

# Loop over data dimensions and create text annotations.
for i in range(len(df.index)):
    for j in range(len(df.columns)):
        try:
            val = int(df.iloc[i, j])
        except:
            val = ''
        text = ax.text(j, i, val,ha="center", va="center", color="white")

plt.title(str(numDays)+" Days of Activities", loc='center')
plt.show()