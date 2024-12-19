import random
random_number = random.randint(1,50)
count = 1
while True:
    guess = int(input("Enter the number you guess.. "))
    if guess == random_number:
        print("Found")
        print(count)
    elif guess<random_number:
        print("Too low..")
    elif guess>random_number:
        print("Too high")
    count+=1
    play = input("Continue yes//no")
    if play == "no":
        break
