
print('---- create and print tuple -----')
employee_tuple = (101, 'Ahmed Essam', 7000.0, 'Cairo')
print(employee_tuple)
print(type(employee_tuple))


print('---------- access element in a tuple by index -------------') # index like [] in list
print(employee_tuple[0])
print(employee_tuple[-1])

print('------------ un packing tuple ----- ') # variables declared on left while tuple on right
person_id,person_name,salary,city = employee_tuple
print(person_id)
print(person_name)
print(salary)
print(city)


print('------ for i Loop over Tuple -------')
for i in range (len(employee_tuple)):
    print(employee_tuple[i])

print('------ for each item Loop over Tuple -------')
for item in employee_tuple:
    print(item)





