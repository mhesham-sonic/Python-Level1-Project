print('---------------------from file to list-------------------')
list1 = []
with open("C:\\my_files\\read_data.txt", 'r') as file:
    lines = file.readlines()
    for item in lines:
        item = item.strip()
        if item != '':
            list1.append(item)
print(list1)
