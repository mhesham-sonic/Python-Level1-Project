import csv
print('-------------------read from file & filter & write on another file-----------------')

input_file = "C:\\my_files\\people.csv"
output_file = "C:\\my_files\\people_cairo.csv"

with open(input_file,'r') as read_from_file, open(output_file,'w',newline='') as writer_to_file:
    read_from_csv = csv.reader(read_from_file)
    write_to_csv = csv.writer(writer_to_file)
    write_to_csv.writerow(['Name', 'Age', 'City'])
    for row in read_from_csv:
        if row[2] == 'Cairo':
            write_to_csv.writerow(row)
