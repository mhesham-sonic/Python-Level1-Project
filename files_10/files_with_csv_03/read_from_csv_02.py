import csv
print('---------------------read from csv------------------')

with open("C:\\my_files\\people.csv", 'r') as file:
    read_from_csv = csv.reader(file)
    for row in read_from_csv:
        print(row)
