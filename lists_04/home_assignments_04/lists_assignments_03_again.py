print('---------------Checking if an element exist in list or not----------------')

target_no = int(input('Please Insert Target Number: '))
numbers_list = [1, 6, 3, 5, 3, 4]
indexes_list = []
is_found = False
for i in range(len(numbers_list)):
    if numbers_list[i] == target_no:
        # print('numbers is found at : ', i)
        indexes_list.append(i)
        is_found = True

if not is_found:
    print('No. is not Found')
else:
    print(target_no, ' Number is found at : ', indexes_list)
