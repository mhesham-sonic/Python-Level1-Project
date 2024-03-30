# program to show employee data

employee_id = 101
employee_name = 'Yahia'
employee_job = 'Software Engineer'
employee_salary = 135000.00

print('-------------------concat with strings------------')
print(employee_name + ' works as ' + employee_job)

print('----------------------- concat with int or float to string---------------')
# Convert from data type to another [ Casting ]
print(employee_name + " has " + str(employee_id))

print('-----------------------casting from float to int to remove decimal-------------')
invoice_total = 7859.65
print(invoice_total)
print(int(invoice_total))

print('-------------round-------------------')
print(round(invoice_total))
invoice_total = 7859.66
print(round(invoice_total,1))
