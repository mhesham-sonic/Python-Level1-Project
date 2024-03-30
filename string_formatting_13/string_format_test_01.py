print('--------------Test string format-------------------')
emp_id = 101
emp_name = 'Mohamed Hesham'
salary = 3000.768

print('--------------print with concat-----------')
print('Emp has id= ' + str(emp_id) + ', his name= ' + emp_name + ',and his salary= ' + str(salary))

print('-------- print with multi parameters ----------')
print('Emp has id= ', emp_id,', his name= ', emp_name, ', and his salary= ', salary)

print('----------- string formatting using placeholders -----------')  # d integer & s string & f float
print('Emp has id = %d, his name = %s, and his salary = %.2f' %(emp_id, emp_name, salary))

print('------ string formatting using format function ------')  # order inside format is a must
print('Emp has id = {:d}, his name = {:s}, and his salary = {:.2f}'.format(emp_id, emp_name, salary))


print('-------- string formatting using F-String function -------')
print(f'Emp has id = {emp_id}, his name={emp_name}, and his salary = {salary:.2f}')

