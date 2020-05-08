import random
import numpy as np
random.seed(0)

outcomes = np.zeros(13)
numRolls = 1000000
percentCheck = numRolls / 100
print(percentCheck)

outcomeMatrix = np.zeros((13,13))

for i in range(numRolls):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d3 = random.randint(1,6)
    d4 = random.randint(1,6)

    outcomes[d1+d2] += 1
    outcomes[d1+d3] += 1
    outcomes[d1+d4] += 1
    outcomes[d2+d3] += 1
    outcomes[d2+d4] += 1
    outcomes[d3+d4] += 1

    outcomeMatrix[d1+d2,d3+d4] += 1
    outcomeMatrix[d1+d3,d2+d4] += 1
    outcomeMatrix[d1+d4,d2+d3] += 1

    if(i%percentCheck == 0):
        print(i/percentCheck)

numSpaces = [1,1,3,5,7,9,11,13,11,9,7,5,3]

print("PROBABILITIES")
for i in range(2,13):
    prob = outcomes[i]/(numRolls*6)
    print(str(i) + " : " + str(prob) + " : " + str(prob/numSpaces[i]))

print("outcomeMatrix")
for i in range(2,13):
    for j in range(2,13):
        print(outcomeMatrix[j,i], end=", ")
    print("")