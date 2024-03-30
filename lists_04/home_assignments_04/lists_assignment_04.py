print('---------------Program print no. of element occurrence ----------------')

target_no = int(input('Please Insert Target Number: '))
numbers_list = [1, 6, 3, 6, 3, 6]
no_count = 0

for i in range(len(numbers_list)):
    if numbers_list[i] == target_no:
        print(target_no, ' is found in list at position ', i)
        no_count = no_count + 1

print('No of occurrence of ',target_no, ' = ', no_count)