FILE_PATH = "L:/Work/data/Carryover/DCBathIncNoPump/KO.csv"
lineNum = 800*(1/0.0125)
with open(FILE_PATH,'r') as f:
    i=0
    for line in f:
        i=i+1
        if(i>lineNum):
            print(line)
            print()
        if(i>lineNum+5):
            break

