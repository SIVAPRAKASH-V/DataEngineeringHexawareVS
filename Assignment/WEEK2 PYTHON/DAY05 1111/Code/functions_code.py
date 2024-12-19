# Mapping Function 
numbers = [1, 2, 3, 4] 
squared = map(lambda x: x ** 2, numbers) 
print(list(squared)) 

# String Function 
text = "hello world" 
print(text.upper())      

print(text.replace("world", "Python"))  # Output: hello Python 

# Number Function 
num = -7.5 
print(abs(num))          
print(round(3.14159, 2)) # Output: 3.14 

# Date and Time Function 
 
from datetime import datetime 
now = datetime.now() 
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# Python Functions 

def greet(name): 
    return f"Hello, {name}!" 
print(greet("Alice")) 

# Default Argument Values 
def greet(name="Guest"): 
    return f"Hello, {name}!" 
print(greet())          
print(greet("Alice"))   # Output: Hello, Alice! 

# Keyword Arguments 
 
def introduce(name, age): 
    print(f"My name is {name} and I am {age} years old.") 
introduce(age=25, name="Alice") 

# Special Parameters 
 
def func(a, b, /, c, *, d): 
    print(a, b, c, d) 
func(1, 2, c=3, d=4)  

# Arbitrary Argument Lists 

def add_all(*args): 
    return sum(args) 
print(add_all(1, 2, 3, 4))  # Output: 10 

def display_info(**kwargs): 
    for key, value in kwargs.items(): 
        print(f"{key}: {value}") 
display_info(name="Alice", age=25) 

# Lambda Expressions 

square = lambda x: x ** 2 
print(square(5))   # Output: 25 
# Using with filter function 
numbers = [1, 2, 3, 4, 5] 
evens = list(filter(lambda x: x % 2 == 0, numbers)) 
print(evens)  # Output: [2, 4]