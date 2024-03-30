print('--------------Iteration on list for specific number----------')

list1 = [75, 91, 80, 54, 59, 12, 3]
target_no = 54

for item in list1:
    if item == target_no:
        print(target_no, 'is found at ', list1.index(item))
        break
else:
    print(target_no, 'is not found at list1')