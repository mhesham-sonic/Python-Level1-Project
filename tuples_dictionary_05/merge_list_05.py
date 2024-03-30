print('-------------Merging list of keys with list of values in 1 dict-----------')

employee_ids_list = [101, 102, 103]
employee_name_list = ['Ahmed','Mohamed','Yara']
dict_employees = {}
count = 0

for item in employee_ids_list:
    dict_employees[item] = employee_name_list[count]
    count = count + 1

print(dict_employees)