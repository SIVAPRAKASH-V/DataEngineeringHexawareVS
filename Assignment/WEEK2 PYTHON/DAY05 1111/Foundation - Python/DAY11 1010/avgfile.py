file = open('DAY11 1010/stud.txt', 'r')
file_content = file.read()
print(file_content)
file.close()

total=0
student=0
with open('DAY11 1010/stud.txt','r') as file:
    next(file)
    for line in file:
        name,mark = line.strip().split(',')
        total += int(mark)
        student+=1
    avg = int(total)/int(student)
    print(avg)