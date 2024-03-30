print('--------------------first Occurrence of element in list------------')

list1 = [1, 3, 4, 3, 6, 7, 3, 9]
target_no = 3
for i in range(len(list1)):
    if list1[i] == target_no:
        print(target_no, 'is at index', i)
        break
else:
    print(target_no, ' Not found')
