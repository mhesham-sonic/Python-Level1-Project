print('----------------Counting male & female employees tuples from list----------------------')

company_employees = [
(101, 'Hayam Esam', 10000.0, 'Engineer', 'F'),
(102, 'Ibrahim Ahmed', 9000.0, 'Accountant', 'M'),
(103, 'Adham Aly', 5000.0, 'Engineer','M'),
(104, 'Islam Hassan', 7000.0, 'Sales','M'),
(105, 'Marwa Esam', 7000.0, 'Marketer','F'),
(106, 'Ola Hassan', 7000.0, 'Engineer','F')
]

male_count = 0
female_count = 0

for item in company_employees:
    if item[4] == 'M':
        male_count = male_count + 1
    elif item[4] == 'F':
        female_count = female_count + 1

print('Number of Male Employees= ', male_count)
print('Number of Female Employees=', female_count)