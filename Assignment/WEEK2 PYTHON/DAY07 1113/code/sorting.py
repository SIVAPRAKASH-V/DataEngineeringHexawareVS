# sort without key
numbers = [1,5,3,2,8,5,4,9,1,3]
numbers.sort()
print(numbers)
#################################################################

# reverse
number = [2,9,6,4,8,3,6]
number.sort(reverse=True)
print(number)
num = [4,6,4,3,9,7,3,1]
#################################################################

# Sorted
print(sorted(num))
print(sorted(num,reverse=True))
#################################################################


# Sort with key
my_list = [(1, 3), (4, 2), (2, 1)]

# Sort by the second element of each tuple
sorted_list = sorted(my_list, key=lambda x: x[1])
print(sorted_list)
#################################################################

strs = ['a','eeee','cc','dd','r']
sorted_l = sorted(strs, key=len)
print(sorted_l)
#################################################################

strs = ['a','AA','cc','SSS','r','AAA','Z','RER']
sorte_l = sorted(strs, key=str.lower)
print(sorte_l)

#################################################################

def myFun(strs):
    return strs[-1]
#  Sorting string based on last character
strs=['av','Gc','WWa','Sb','Dz','sA','sR','Sr','GSt','gSt']
print(sorted(strs,key=myFun))
#################################################################
