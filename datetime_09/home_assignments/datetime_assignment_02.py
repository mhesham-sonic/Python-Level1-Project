from datetime import datetime
from dateutil import relativedelta
print('---------------Check if a specific date exists in a list of dates -----------')

given_date = datetime(2023, 8, 15)
dates_list = [datetime(2023, 12, 31),
              datetime(2023, 8, 15),
              datetime(2023, 5, 1)]
isfound = False
for i in range(len(dates_list)):
    if given_date == dates_list[i]:
        isfound = True
        print(f'{given_date} is found at index {i}')

if not isfound:
    print('Not Found')
