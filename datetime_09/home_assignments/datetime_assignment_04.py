from datetime import datetime
from dateutil import relativedelta
print('---------------Count occurrences of a specific date in a list-----------')

dates_list = [
    datetime(2023, 12, 31),
    datetime(2023, 8, 15),
    datetime(2023, 8, 15),
    datetime(2023, 5, 1)
]
given_date = datetime(2023, 8, 15)
count = 0

for i in range(len(dates_list)):
    if dates_list[i] == given_date:
        count += 1
print(f'{given_date} occurs {count} times')