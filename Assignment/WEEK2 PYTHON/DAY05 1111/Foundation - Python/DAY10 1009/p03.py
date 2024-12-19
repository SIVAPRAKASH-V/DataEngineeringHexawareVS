
def addition_mul(*args): # * before the argument args shows it is a multi/variable length argument; This accepts only values; this behaves as a tuple
    result = 0
    for num in args:
        result += num
    return result
   
 
print(addition_mul(1,2,345,223,532,12,432))
print(addition_mul(56,33))
print(addition_mul(56,33,25,26,32))



def user_profile(**kwargs): # ** before the argument kwargs shows it is a multi/variable length keyword argument; This accepts key value pairs; this behaves as a dictionary
    for key, value in kwargs.items():
        print("{} has {}".format(key, value))

user_profile(name="HRB", mobile=8825410600, city="Chennai")
user_profile(name="Hiran Ram Babu", email="info@mjit.in", city="Chennai")