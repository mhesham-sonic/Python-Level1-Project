from datetime import datetime
from dateutil import relativedelta

print('----------Get date after 12 working days--------------')

input_date = datetime.now()
jump_days = 12
for i in range(jump_days):
    if input_date.weekday() == 3:
        input_date = input_date + relativedelta.relativedelta(days=3)
    elif input_date.weekday() == 4:
        input_date = input_date + relativedelta.relativedelta(days=2)
    else:
        input_date = input_date + relativedelta.relativedelta(days=1)
print(input_date)
