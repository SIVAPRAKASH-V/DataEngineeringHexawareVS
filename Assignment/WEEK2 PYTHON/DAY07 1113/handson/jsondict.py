import json

with open('my_file.json') as json_file:
 data = json.load(json_file)
 print(data)
 
 print("TYPE:", type(data))

