# import datetime # this is to call a module; a complete module; import module
# print(datetime.datetime.now())
 
from datetime import datetime # this is to call a function/class of a module ; from module import function/class
print(datetime.now())
  
# Date and Time - datetime module.
 
import datetime # this is to call a module; a complete module; import module
print(datetime.datetime.now())
 
# from datetime import datetime # this is to call a function/class of a module ; from module import function/class
# print(datetime.now())
 
print(datetime.date.today())
 
print(datetime.datetime.now().strftime("%d-%m-%Y")) # format date time type
 
 
date_time = "2024-10-09 11:43:45"
print(type(date_time))
date_time_proper = datetime.datetime.strptime(date_time,"%Y-%m-%d %H:%M:%S") # Convert string to date time type
# print(type(datetime.datetime.strptime(date_time,"%Y-%m-%d %H:%M:%S"))) # Convert string to date time type
date_proper = date_time_proper.strftime("%d")
print("Current Date is",date_proper)
 
 


from datetime import datetime
import time
def greet_guests():
    current_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    print("Hey guest, Thanks for coming!")
    print("You have been logged in at {}".format(current_time))

greet_guests()
time.sleep(5)
greet_guests()
time.sleep(5)
greet_guests()
time.sleep(5)
greet_guests()






def greet_guests(name):
    current_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    print("Hey {}, Thanks for coming!".format(name))
    print("You have been logged in at {}".format(current_time))
 
greet_guests("Hiran")
time.sleep(5)
greet_guests("HRB")
time.sleep(5)
greet_guests("Vignesh")
time.sleep(5)
greet_guests("Vinothini")


def greet_guests(name="guest"):
    current_time = datetime.now().strftime("%d-%m-%y %H:%M:%S")
    print("Hey {}, Thanks for coming!".format(name))
    print("You have been logged in at {}".format(current_time))

greet_guests("Hiran")
time.sleep(1)
greet_guests("HRB")
time.sleep(1)
greet_guests()
time.sleep(1)
greet_guests("Vinothini")

def addition(num1,num2):
    result = num1+num2
    print("The result of addition of {} and {} is {}".format(num1, num2, result))

def get_multiplication_table(num1,num=3):
    result = num1*num
    print("The multiplication of {} table by {} is {}".format(num,num1,result))

addition(7,8)
addition(75,15787)
addition(0,0)
get_multiplication_table(5)
get_multiplication_table(6,2)



def addition_mul(*args): # * before the argument args shows it is a multi/variable length argument; This accepts only values; this behaves as a tuple
    result = 0
    for num in args:
        result += num
    return result
   
 
print(addition_mul(1,2,345,223,532,12,432))
print(addition_mul(56,33))
print(addition_mul(56,33,25,26,32))
