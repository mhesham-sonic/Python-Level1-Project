print('------- program to create 2 lists [ unique data | duplicate data ] ------')
my_list = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
unique_list = []
duplicated_list = []

for item in my_list:
    if item not in unique_list:
        unique_list.append(item)
    elif item not in duplicated_list:
        duplicated_list.append(item)

print(my_list)
print(unique_list)
print(duplicated_list)