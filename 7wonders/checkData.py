
with open('./7wonders/games.csv', newline='') as csvfile:
    line = csvfile.readline()
    line = csvfile.readline()
    while(line):
        splitData = line.split(sep=",")
        totalPoints = int(splitData[2]) + int(splitData[3]) + int(splitData[4]) + int(splitData[5]) + int(splitData[6]) + int(splitData[7]) + int(splitData[8]) 
        roundNum = int(splitData[0])
        name = splitData[1]
        print("game " + str(roundNum) + "," + name + " : " + str(totalPoints))
        input()
        line = csvfile.readline()

