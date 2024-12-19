subject_marks = {}
name = input("Enter Name: ")
grade = input("Enter Your class: ")
def get_details():

    print("Enter subjects and mark obtained: ")
    while True:
        if ch =='1':
            sub = input("Enter subject name: ")
            mark = int(input("Enter Mark obtained: "))
            subject_marks[sub]=mark
        else:
            break
        ch = input("Enter 1 to add subject: ")



