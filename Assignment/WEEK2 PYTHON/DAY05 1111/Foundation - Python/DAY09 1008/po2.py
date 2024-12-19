"""
list - array - ordered - allow duplicates - mutable (can be updated) - [] - list()
tuple - array - orderd - allows duplicates - immutable (cannot be updated) - () - tuple()
set - array - unordered - will not allows duplicates - muteable (can be updated) - {} - set()
"""
 
list_1 = [1,2,3,4,5, "Hello World", [6,7]]
tuple_1 = (1,2,3,4,5, "Hello World", [6,7])
set_1 = {1,2,3,4,5, "Hello World"}
 
print(list_1)
print(tuple_1)
print(set_1)
 
# print(set_1[3])
 
list_1[3] = 3
# tuple_1[3] = 3
print(tuple_1.count(2))
print(tuple_1.index(2))
print(len(list_1))
print(len(tuple_1))
print(len(set_1))
print(set_1)
 
set_1.add(76)
print(set_1)
set_1.pop()
print(set_1)
set_1.remove(5)
print(set_1)
 
list_1.append("Happy")
print(list_1)
list_1.insert(2, "Happy")
print(list_1)
list_1.extend(["Diwali", 88, 21])
print(list_1)
# list_1.sort()
print(list_1)

list_1.reverse()
print(list_1)
 
print(list_1[1:3])
print(list_1[:4])
print(list_1[2:])
 
