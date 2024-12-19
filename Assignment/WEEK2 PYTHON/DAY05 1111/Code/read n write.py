import csv
with open('my_data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
new_row = [4, 'Rajesh', 30]
data.append(new_row)
with open('my_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)