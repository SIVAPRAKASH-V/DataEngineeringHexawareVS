# read as dict
import json

with open ('data_list.json','r') as data_set:
    data_read = json.load(data_set)
    print(data_read)
    print(type(data_read))
    print(data_read["age"])