print('---------Remove duplicated words ---------')

str1 = 'Hello world world python is great great python'
list1 = str1.split()
print(list1)

unique_list = []
duplicate_list = []

for item in list1:
    if item not in unique_list:
        unique_list.append(item)
    elif item not in duplicate_list:
        duplicate_list.append(item)

str2 = ' '.join(unique_list)
print(str2)

