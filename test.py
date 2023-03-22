import json
with open('data.json', 'r') as myfile:
    data = json.load(myfile)
shows=[]
for i in data["show"]:
    shows.append(i)
print(shows)

        