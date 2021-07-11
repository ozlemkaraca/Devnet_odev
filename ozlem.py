import json
file=open("ozlem.json","r")
json_file=json.load(file)

for a,b in json_file["kimlik"].items():
	print(a,b)
