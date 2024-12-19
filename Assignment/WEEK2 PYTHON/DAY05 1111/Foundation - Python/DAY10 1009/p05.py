def user_profile(name,age,*args,**kwargs):
    print("Name: {}".format(name))
    print("Age: {}".format(age))
    if args:
        print("Args items:")
        for val in args:
            print(val)
    if kwargs:
        print("Kwargs items:")
        for key, value in kwargs.items():
            print("{}: {}".format(key, value))

# user_profile("HRB",25, "BE EIE", "Indian", mobile=8825410600, city="Chennai")
# user_profile("Hiran Ram Babu", 34, "KLNCE Student", "Automation Architect", email="info@mjit.in", city="Chennai")
user_profile("Vignesh", 22, profession="Student", College="KLNCE")



# lambda - anonymous function - no name function.
# map(), filter(), reduce()
# lambdaa args: expr

mul_tab_3 = lambda temp: temp * 3

print(mul_tab_3(6))
print(mul_tab_3(10))
print(mul_tab_3(5))
print(mul_tab_3(22))




# map() function - iterable item - new iterable item
# input - List; action - lambda function; output - list
multipliers = [1,2,3,4,5,6]
mul_tab_3 = map(lambda temp: temp * 3, multipliers)
print(list(mul_tab_3))

# filter() function - iterable item - true/false
# input - list; action - lambda action to filter with condition; output - list with True cases
# filter(function, iterable)

all_numbers=[12,34,12,432,123,344,5213,54,66,54,67,89,201]
# filter only the even number
even_numbers = filter(lambda temp: (temp % 2) == 0, all_numbers)
print(list(even_numbers))


# reduce function - iterable - reduce the provided iterable items to a single output; functools module
# input - list; action - expr/binary function - operates with 2 values ; output - single value
# reduce(function, iterable)

from functools import reduce
input_numbers = [12,21,123,432,532,23,55]

addition_input_numbers = reduce(lambda temp1, temp2: temp1 + temp2, input_numbers)
print(addition_input_numbers)

# multiplier of 3 with multi inputs but the 
# result needs to be only for the odd numbers; 
# even numbers must not be included! use map and filter

input_numbers = [12,21,123,432,532,23,55]

print("TASK....")
all_numbers=[12,34,12,432,123,344,5213,54,66,54,67,89,201]
# print(list(even_numbers))
multi = list(map(lambda temp1 : temp1 * 3, filter(lambda temp: (temp % 2) != 0, all_numbers)))
# mul = list(multi)
# print(mul)
addi = reduce(lambda temp1, temp2: temp1 + temp2, multi)  # Add 0 as the initial value

# print(list(multi))
print(addi)


# addi = reduce(lambda temp1, temp2: temp1 + temp2, list(multi))
# print(addi)

def is_prime(num):
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

# Example usage:
number = addi
if is_prime(number):
  print(number, "is a prime number")
else:
  print(number, "is not a prime number") 