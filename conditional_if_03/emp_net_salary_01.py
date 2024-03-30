print('------------------program to calculate employee salary based on conditional if--------')

emp_gross_salary = 7000
if emp_gross_salary > 5000:
    tax = 0.1
else:
    tax = 0

emp_net_monthly_salary = emp_gross_salary - (emp_gross_salary * tax)
emp_annual_salary = emp_net_monthly_salary * 12

print('Employee Monthly Net Salary= ', emp_net_monthly_salary)
print('Employee Monthly Net Salary= ', emp_annual_salary)
