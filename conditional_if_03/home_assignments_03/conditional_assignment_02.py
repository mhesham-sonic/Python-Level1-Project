print('-----------Program to calculate Employee Bonus based on conditional IF-----------')

emp_salary = float(input('Please Enter Employee Salary: '))

if emp_salary >= 5000:
    bonus = 2000
else:
    bonus = 4000

emp_salary_with_raise = emp_salary + bonus

print('Employee Salary Before Raise= ', emp_salary)
print('Bonus= ', bonus)
print('Employee Salary After Raise= ', emp_salary_with_raise)

