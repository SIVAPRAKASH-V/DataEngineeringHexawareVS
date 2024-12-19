# read as list for multiple data present in json 
import json

with open ('data.json','r') as data_set:
    data_read = json.load(data_set)
    print(data_read)
    print(type(data_read))
    print(data_read[1]["subjects"])