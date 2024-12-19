import csv
filepath='my_data.csv'
with open(filepath,'w+',newline="") as file:
    csvwriter=csv.writer(file)
    csvwriter.writerow(["Id","Name","Age"])
    data=[[6,"Kavin",20],
    [7,"Ramesh",19]]
    csvwriter.writerows(data)
    print("writing had been completed")