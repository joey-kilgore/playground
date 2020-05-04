
FILE_PATH = "C:/Users/Joey Kilgore/Desktop/modified_headban-25d.gcode"
inFile = open(FILE_PATH, 'r')

FILE_PATH = "C:/Users/Joey Kilgore/Desktop/multiPrint.gcode"
outFile = open(FILE_PATH, 'w+')

Lines = inFile.readlines() 

# we need to change the extruder value for every line of the second print
# for print 1, the first extruder command was to set the extruder to 38.31917
#   the last extruder command was to 7010.03367
#   an additional 5 is added to extrude prior to the start of the print
extruderOffset = 7010.03367 - 38.31917 + 5

lineNum = 0

for line in Lines[:110236]:
    lineNum += 1
    if(lineNum%100 == 0):
        print(lineNum)
    outFile.write(line)

for line in Lines[110236:220003]:
    lineNum += 1
    if(lineNum%100 == 0):
        print(lineNum)
    parts = line.split(' ')
    newParts = []
    for part in parts:
        if('E' in part):
            try:
                num = float(part[1:])
                num += extruderOffset
                part = 'E' + str(round(num,5)) + '\n'
            except:
                print("exception caught")
        newParts.append(part)  
    output = ' '.join(newParts)
    outFile.write(output)

for line in Lines[220003:]:
    lineNum += 1
    if(lineNum%100 == 0):
        print(lineNum)
    outFile.write(line)

outFile.close()