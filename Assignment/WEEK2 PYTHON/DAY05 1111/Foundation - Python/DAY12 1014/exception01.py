# Exception Handling
# Instead the system/python gives the error and abruptly stops, We give a graceful exit
# This is the actual way to hande the key, value, type, index, zero etc mistakes

try:
    pass # we think, the lines of code, which may throw/raise exception #Code
except:
    pass # if exception occurs, handle gracefull here
except ValueError as e: # e as a argument
    print("The error is {}".format(e)) # usage of the temp argument e within the exception block
    pass
except TypeError as typeErr: # Error Type - Type error - Datatype
    pass
except IndexError: # Index of a subscritable
    pass
except KeyError: # error in a dictionary
    pass
except ZeroDivisionError: # divisible by 0 error
    pass
else:
    pass # This block is used, when no exception occurs # Excute as a result of successful try
finally:
    pass # This executes, the code in try is success/failure. This is majorly used to clean things up.



#####################################################


# num_1 = int(input("Enter a number: "))
# print(75/num_1)
try:
    num_1 = int(input("Enter a number: "))
    print(75/num_1)
except:
    print("Some error occured!!!!")

#####################################################



# num_1 = int(input("Enter a number: "))
# print(75/num_1)
try:
    num_1 = int(input("Enter a number: "))
    print(75/num_1)
except ZeroDivisionError as zde:
    print("Please do not enter 0; we need some positive integers!!")
    print("Actual error is: {}".format(zde))
except ValueError as ve:
    print("Please do not enter strings; we need some positive integers!!")
    print("Actual error is: {}".format(ve))
except:
    print("Some error occured!!!!")


#####################################################

# num_1 = int(input("Enter a number: "))
# print(75/num_1)
try:
    num_1 = int(input("Enter a number: "))
    print(75/num_1)

except Exception as e:
    print("Some error occured!!!! - {}".format(e))



try:
    num_1 = int(input("Enter a number: "))
    print(75/num_1)
except ZeroDivisionError as zde:
    print("Please do not enter 0; we need some positive integers!!")
    print("Actual error is: {}".format(zde))
except ValueError as ve:
    print("Please do not enter strings; we need some positive integers!!")
    print("Actual error is: {}".format(ve))
except Exception as e:
    print("Some error occured!!!! - {}".format(e))
else:
    print("75 is divisible with {}".format(num_1))
finally:
    print("Thanks for listening!")

#################################################################################


try: # like open a file
    num_1 = int(input("Enter a number: "))
    print(75/num_1)
except ZeroDivisionError as zde: # Different exceptions to be handled
    print("Please do not enter 0; we need some positive integers!!")
    print("Actual error is: {}".format(zde))
except ValueError as ve:
    print("Please do not enter strings; we need some positive integers!!")
    print("Actual error is: {}".format(ve))
except Exception as e:
    print("Some error occured!!!! - {}".format(e))
else: # File tasks in successfull opening of a file
    print("75 is divisible with {}".format(num_1))
finally: # File closure operation
    print("Thanks for listening!")



####################################################################

try:
    file = open("test.txt", 'r')
except Exception as e:
    print("Sorry, some issue occured. The error - {}".format(e))
else:
    file_content = file.read()
    print(file_content)
    file.close()

###########################################################

def check_age():
    if age >= 18:
        print("Great! you can proceed with login")
    else:
        # print("You need to be minimum 18 years old to signup with our App!")
        raise ValueError("Age must be atleast 18.")

try:
    age = int(input("Enter the Age to login: "))
    check_age()
except ValueError as ve:
    print(ve)
except Exception as e:
    print(e)


###########################################%%%%%%%%%%%%%%%%%%
class OutOfStockError(Exception):
    pass

def apply_coupon(cart, coupon_code):
    if coupon_code == "INVALID":
        raise ValueError("Invalid coupon code!")
    else:
        print("Coupon applied successfully")

def checkout(cart, stock):
    if cart > stock:
        raise OutOfStockError("Not enough stock available!")
    else:
        print("Checkout successful")

try:
    apply_coupon(["item1"], "INVALID")
except ValueError as e:
    print(e)

try:
    checkout(5, 2)
except OutOfStockError as e:
    print(e)
 
