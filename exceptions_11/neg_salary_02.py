import sys
print('----------------Negative Salary Exception-------------')
try:
    salary = float(input('Please Enter Employee Salary: '))
    if salary < 0:
        raise Exception

    if salary > 5000:
        bonus = 1000
    else:
        bonus = 3000
    net_salary = salary + bonus
    print('Net Salary is: ', net_salary)

except Exception as arg:
    print('Negative salary', arg)
    sys.exit()

