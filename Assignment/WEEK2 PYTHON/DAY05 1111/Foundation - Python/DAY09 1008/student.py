# name = input("Enter name: ")
# # regno = input("Enter regno: ")
# mark1 = input("Enter mark1: ")
# mark2 = input("Enter mark2: ")
# mark3 = input("Enter mark3: ")

# # print(name)
# # print(regno)3
# total = int(mark1)+int(mark2)+int(mark3)
# # print("Total Mark {}".format(total))
# average = (total)/3
# print("Average mark: {}".format(average))
# num = int(input("Enter num: "))

# if(num%3==0):
#     print(num/3)
# else:
#     print("Not divisible!")


# name = input("Enter name: ")
# age = int(input("Enter regno: "))
# height = int(input("Enter mark1: "))
# weight = int(input("Enter mark2: "))

while(input("press n to stop - ")!='n'):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    height = float(input("Enter height: "))
    weight = float(input("Enter weight: "))

    bmi = float(weight/height**2)
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi < 25:
        print("You have a normal weight.")
    elif bmi >= 25 and bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")

    
    