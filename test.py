import json
with open('data.json', 'r') as myfile:
    data = json.load(myfile)

#print((data["user"][0]["username1"]))
deta=(data["user"][0:])

print(deta)