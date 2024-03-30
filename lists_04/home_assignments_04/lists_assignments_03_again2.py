print('---------------Checking if an element exist in list or not print only first occurrence ----------------')

target_no = int(input('Please Insert Target Number: '))
numbers_list = [1, 6, 3, 5, 3, 4]

is_found = False
for i in range(len(numbers_list)):
    if numbers_list[i] == target_no:  # and is_found == False:
        print('numbers is found at : ', i)
        is_found = True
        break

if not is_found:
    print('No. is not Found')
