# THIS IS A SOLUTION TO
# https://www.codechef.com/problems/TYPING


def getTrials():
    return int(input())

def getTimeTrial():
    numWords = int(input())
    knownWords = []
    leftHand = 'df'
    rightHand = 'jk'
    nextWord = ''
    time = 0
    for wordNum in range(numWords):
        nextWord = raw_input()
        wordTime = 2
        for i in range(len(nextWord)-1):
            if (nextWord[i] in leftHand and nextWord[i+1] in leftHand) or (nextWord[i] in rightHand and nextWord[i+1] in rightHand):
                wordTime += 4
            else:
                wordTime += 2
        if nextWord in knownWords:
            time += wordTime/2
        else:
            time += wordTime
            knownWords.append(nextWord)
    return time

def main():
    numTrials = getTrials()
    for trial in range(numTrials):
        time = getTimeTrial()
        print(time)

main()
