print('---------------------swapping elements in the list------------')

newList = [12, 35, 9, 56, 24]
print(newList)
initial_first_item = newList[0]
initial_last_item = newList[-1]
newList[0] = initial_last_item
newList[-1] = initial_first_item
print(newList)

