import json

jsonstring = '{ "id": 121, "name": "Naveen", "course": "MERN Stack"}'
 
student_data =json.loads(jsonstring)
 
print(student_data)
print(type(student_data))
print(student_data['name'])
print(student_data['course'])

