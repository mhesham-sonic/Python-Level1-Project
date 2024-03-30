print('---------------Checking if an element exist in list or not----------------')

target_no = int(input('Please Insert Target Number: '))
numbers_list = [1, 6, 3, 5, 3, 4]
value_found = 0
for i in range(len(numbers_list)):
    if numbers_list[i] == target_no:
        print(target_no, ' is found in list at position ', i)
        value_found = 1
    elif numbers_list[i] != target_no and i == len(numbers_list)-1 and value_found == 0:
        print('Not Found')