from datetime import datetime
from dateutil import relativedelta
print('---------------Find the earliest (oldest) date from a list of dates -----------')

dates_list = [datetime(2023, 12, 31),
              datetime(2023, 8, 15),
              datetime(2023, 5, 1)]

oldest_date = dates_list[0]

for i in range(len(dates_list)):
    if dates_list[i] < oldest_date:
        oldest_date = dates_list[i]
print(f'Oldest date = {oldest_date} ')
