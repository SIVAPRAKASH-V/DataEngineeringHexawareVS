# If 
x = 10 
if x > 5: 
    print("x is greater than 5") 

# If-else
x = 3 
if x > 5: 
    print("x is greater than 5") 
else: 
    print("x is 5 or less") 


# If-Elif-Else Statement 
x = 7 
if x > 10: 
    print("x is greater than 10") 
elif x > 5: 
    print("x is greater than 5 but not greater than 10") 
else: 
    print("x is 5 or less")


# For loop
for i in range(3): 
    print(i)

# while loop
x = 0 
while x < 3: 
    print(x) 
    x += 1

# Nested loop
for i in range(2): 
    for j in range(3): 
        print(f"i={i}, j={j}")

# Break pass continue
for i in range(5): 
    if i == 2: 
        continue  # Skip 2 
    elif i == 4: 
        break   # Stop the loop at 4 
    else: 
        print(i)

# Input n output
name = input("Enter your name: ") 
print("Hello, " + name)

# List
fruits = ["apple", "banana", "cherry"] 
print(fruits) 

# List methods n slicing
fruits = ["apple", "banana", "cherry"] 
fruits.append("orange") 
print(fruits[1:3])  # Slicing from index 1 to 2 


# Introduction to Dictionaries & Dictionary Methods 
person = {"name": "Alice", "age": 25} 
print(person["name"]) 
# Dictionary methods 
person["age"] = 26  # Update value 
print(person.get("age")) 

# Introduction to Set & Set Methods 
numbers = {1, 2, 3, 3}  # Duplicates are removed 
numbers.add(4) 
print(numbers) 

# Introduction to Map & Map Methods 
numbers = [1, 2, 3, 4] 
squared = map(lambda x: x ** 2, numbers) 
print(list(squared)) 

