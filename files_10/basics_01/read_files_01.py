print('-------------------How to Read files----------------')

print('-------------------Method-1----------------')
file1 = open("C:\\my_files\\read_data.txt", 'r')
data1 = file1.read()
print(data1)
file1.close()

print('-------------------Method-2----------------')
file2 = open("C:\\my_files\\read_data.txt", 'r')
for item in file2:
    print(item, end='')
file2.close()


print('\n-------------------Method-3----------------')
with open("C:\\my_files\\read_data.txt", 'r') as file3:
    data3 = file3.read()
print(data3)



