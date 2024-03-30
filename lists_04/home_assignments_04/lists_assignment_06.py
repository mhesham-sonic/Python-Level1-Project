print('---------------Program to print Min and Max elements in list----------------')

numbers_list = [23, 90, 19, 65]
min_no = numbers_list[0]
max_no = numbers_list[0]
for item in numbers_list:
    if item > max_no:
        max_no = item
    elif item < min_no:
        min_no = item
print('Max number in list is ', max_no)
print('Min number in list is ', min_no)