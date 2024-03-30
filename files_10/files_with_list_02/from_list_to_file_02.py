print('---------------------------from list to file----------------')

my_list = ['Luxor', 'Cairo', 'Alex', 'Cairo']

with open('C:\\MY_FILES\\write_data.txt', 'w') as file3:
    for i in range(len(my_list)):
        if i == len(my_list)-1:
            file3.write(my_list[i])
        else:
            file3.write(my_list[i] + '\n')

new_list = ['Mansoura', 'Giza', 'Assuit']

with open('C:\\MY_FILES\\write_data.txt', 'a') as file3:
    file3.write('\n')  # to start the append with enter in order not to mix with above
    for i in range(len(new_list)):
        if i == len(new_list)-1:
            file3.write(new_list[i])
        else:
            file3.write(new_list[i] + '\n')

print('--- read all data from write_date.txt file > convert to upper and re write to another file --')

with open('C:\\MY_FILES\\write_data.txt', 'r') as file4:
    content1 = file4.read()
    print(content1)
    content2 = content1.upper()
    print(content2)

with open('C:\\MY_FILES\\write_data2.txt', 'w') as file5:
    file5.write(content2)




