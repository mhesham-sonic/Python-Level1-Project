print('----------------Printing sum of salaries of employees tuples from list----------------------')

company_employees = [
(101, 'Ahmed Esam', 10000.0, 'Cairo'),
(102, 'Ibrahim Ahmed', 9000.0, 'Cairo'),
(103, 'Adham Aly', 5000.0, 'Cairo'),
(104, 'Islam Hassan', 7000.0, 'Cairo')
]
sum_of_salaries = 0
for item in company_employees:
    sum_of_salaries = sum_of_salaries + item[2]

print('Sum of Salaries= ', sum_of_salaries)
