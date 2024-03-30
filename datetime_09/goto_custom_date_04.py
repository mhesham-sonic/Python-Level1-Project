from datetime import datetime  # from module datetime import class datetime
from dateutil import relativedelta  # from package dateutil import module relativedelta

print('--------------- go to required date from now------------')

date_today = datetime.now()
first_day = date_today + relativedelta.relativedelta(day=1)
print(first_day)
last_day = date_today + relativedelta.relativedelta(day=31) # if month is 30 days it will automatically update
print(last_day)