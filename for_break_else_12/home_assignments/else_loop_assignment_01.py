print('-------------Iteration on all even numbers---------------')

list1 = [1, 3, 5, 7, 12, 11]

for item in list1:
    if item % 2 == 0:
        print(item, 'is Even Number')
        break
else:
    print('No Even Numbers in list1')
