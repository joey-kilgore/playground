import json

data = {}

FILE_PATH = "L:/Github Repos/playground/Life_Data/daylio_export_2020_04_19.csv"
dataFile = open(FILE_PATH, 'r')

# Using readlines() 
Lines = dataFile.readlines() 
  
count = 0
# Strips the newline character 
for line in Lines[1:]: 
    #print(line.strip()) 
    #print("Line{}: {}".format(count, line.strip())) 
    part = line.split(",")
    dateTime = part[0]
    monthDate = part[1]
    weekDay = part[2]
    time = part[3]
    mood = part[4]
    activities = part[5]
    note = part[6]
    try:
        print(data[dateTime]['monthDate'])
    except:
        data[dateTime] = {
            'monthDate' : monthDate,
            'weekDay' : weekDay
        }


    mock = {
        'mood' : mood,
        'activities' : activities.replace("\"", "").split(" | "),
        'note' : note.replace("\"", "")
    }
    print("BEFORE")
    print(data[dateTime])
    data[dateTime][time] = mock
    print("AFTER")
    print(data[dateTime])
    count += 1

print(data)

with open('daylio.json', 'w') as json_file:
    json.dump(data, json_file)