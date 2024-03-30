from datetime import datetime
from dateutil import relativedelta
print('---------------Create a list of dates within a date range included-----------')
start_range = datetime(2023, 1, 1)
end_range = datetime(2023, 1, 10)
count_date = start_range
dates_list = [count_date]

while count_date < end_range:
    count_date = count_date + relativedelta.relativedelta(days=1)
    dates_list.append(count_date)

print(dates_list)






