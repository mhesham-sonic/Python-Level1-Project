print('---------------- create and print lists -------------------')

numbers_list = [1, 7, 23, 45, 60, 85, 10]
print(numbers_list)
print(type(numbers_list))

print('---------------- Adding Elements to list (append & insert functions) -------------------')
# append will add at the end while insert will add after the specified index starting from 0
numbers_list.append(33)
numbers_list.insert(3,15)
print(numbers_list)

print('---------------- Access Elements to list by index and change the element-------------------')
print(numbers_list[5])
numbers_list[5] = numbers_list[5] + 10
print(numbers_list)

print('---------------- Count Elements in list by len function(general function)-------------------')
print(numbers_list)
print(len(numbers_list))

print('---------------- Delete Elements from list using pop & remove functions-------------------')
# remove work on value while pop work on index and if pop used without index it will remove last element
numbers_list.remove(70)
print(numbers_list)
numbers_list.pop(3) # .pop()        : remove the last element
print(numbers_list)

print('---------------- Reverse Elements of list using reverse function-------------------')
print(numbers_list)
backup_list = numbers_list.copy()
numbers_list.reverse()
print(backup_list)
print(numbers_list)

print('---------------- Sorting Elements of list using sort function-------------------')
# default of sorting is in ascending order
print(numbers_list)
numbers_list.sort()  # asc
print(numbers_list)
numbers_list.sort(reverse=True)  # desc
print(numbers_list)
print('original list = ', backup_list)