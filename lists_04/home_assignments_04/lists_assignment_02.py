print('---------------Program to swap 2 elements in list----------------')

numbers_list = [23, 65, 19, 90]
pos_1 = int(input('Enter Position 1 in list: '))
pos_2 = int(input('Enter Position 2 in list: '))
backup_list = numbers_list.copy()
temp = numbers_list[pos_1]
numbers_list[pos_1] = numbers_list[pos_2]
numbers_list[pos_2] = temp

print('Original List= ', backup_list)
print('New List= ', numbers_list)



