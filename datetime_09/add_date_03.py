
from datetime import datetime  # from module datetime import class datetime
from dateutil import relativedelta  # from package dateutil import module relativedelta

date_today = datetime.now()

print('------ add 1 year , 6 months, 5 days -----')
new_date = date_today + relativedelta.relativedelta(years=1, months=6, days=5)
print(new_date)