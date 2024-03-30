import csv
print('--------------write to csv file----------------')
people_list = [
    ('Name', 'Age', 'City'),
    ('Adham', 25, 'Assuit'),
    ('Esam', 30, 'Cairo'),
    ('Shady', 28, 'Mansoura')
]
with open("C:\\my_files\\people.csv", 'w', newline='') as file:   # remove empty line enter between rows
    write_to_csv = csv.writer(file)
    for row in people_list:
        write_to_csv.writerow(row)   # writerow takes iterable : list/tuple/dict/string/....

print('---------------------Append lists to existing list in csv----------------')

new_data = [['Emad', 29, 'Luxor'], ['Marwa', 33, 'Cairo']]
with open("C:\\my_files\\people.csv", 'a', newline='') as file: 
    write_to_csv = csv.writer(file)
    for row in new_data:
        write_to_csv.writerow(row)

