import requests
import json

response = requests.get("https://api.covid19api.com/summary")

f = open("summary.json", "w+")
f.write(response.text)
f.close()

data = json.load(open("summary.json"))
total = 0
for c in data["Countries"]:
    print(str(c["Country"]) + "," + str(c["TotalDeaths"]))
    total += c["TotalDeaths"]

print(total)