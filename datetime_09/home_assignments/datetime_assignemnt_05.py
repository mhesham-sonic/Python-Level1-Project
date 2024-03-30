from datetime import datetime
from dateutil import relativedelta
print('---------------Check if all dates in a list are in the same month-----------')
dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 12, 15),
    datetime(2023, 12, 15),
    datetime(2023, 12, 1)
]
check = False
x = dates_list[0].month
for i in range(len(dates_list)):
    if dates_list[i].month == x:
        check = True
if check:
    print(f'All Dates are in the same Month:{x}')
else:
    print('Not All the dates are in same month')
