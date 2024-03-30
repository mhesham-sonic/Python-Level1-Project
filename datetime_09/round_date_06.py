from datetime import datetime
from dateutil import relativedelta

print('---------------------get rounded date------------------------')

input_date = datetime(day=14, month=3, year=2024)
print(input_date)

if input_date.day >= 15:
    round_date = input_date + relativedelta.relativedelta(months=1, day=1)
else:
    round_date = input_date + relativedelta.relativedelta(day=1)  # current month

print('Rounded Date is', round_date)
