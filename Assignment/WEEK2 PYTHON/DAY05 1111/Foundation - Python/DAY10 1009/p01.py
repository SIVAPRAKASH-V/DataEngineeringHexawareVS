# Dictionary - Key Value - {} - mutable - unordered - Indexed with keys - Keys needs to be unique, values can be of any datatype
dict_1 = {
    'name': "Hiran Ram Babu",
    'age': 34,
    'experience': ["TechM", "Accenture", "Capgemini", "Maho Jase IT"]
}
 
print(dict_1)
 
# Dictionary - Key Value - {} - mutable - unordered - Indexed with keys - Keys needs to be unique, values can be of any datatype
dict_1 = {
    'name': "Hiran Ram Babu",
    'age': 34,
    'experience': ["TechM", "Accenture", "Capgemini", "Maho Jase IT"],
    'workLocation': ("Hyderabad", "Bengaluru",600100,625020),
    'Skills': {
        'FrontEnd': 'React.js',
        'Backend': 'Python Django',
        'Automation': ['Python','Powershell']
    }
}
 
print(dict_1)
 
# Dictionary Functions
print(dict_1['age'])
print(dict_1.get('name'))
 
dict_1['mobile'] = 8825410600 #addtion
dict_1['age'] = 35 #updatation

dict_1['age'] # removes specified key value paid but do not return anything
 
print(dict_1)
 
delMobile = dict_1.pop('mobile') # Removes specified key Value pair
print(delMobile)
 
delLast = dict_1.popitem() # Removes the last added key value pair
print(delLast)
print(dict_1)


print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())
print(dict_1)
 
dict_2 = {'name': 'HRB', 'age': 34, 'experience': ['TechM', 'Accenture', 'Capgemini', 'Maho Jase IT'], 'workLocation': ('Hyderabad', 'Bengaluru', 600100, 625020), 'Skills': {'FrontEnd': 'React.js', 'Backend': 'Python Django', 'Automation': ['Python', 'Powershell']}, 'mobile': 8825410600}
 
dict_1.update(dict_2)
print(dict_1)
 
