import datetime
from datetime import datetime  # from module datetime import class datetime
from dateutil import relativedelta  # from package dateutil import module relativedelta

print('------- get difference between 2 dates [ in days ] using datetime class ------')
date_today = datetime.now()
custom_date = datetime(year=2022,month=12,day=20)
diff_days = date_today - custom_date
print(diff_days.days)

print('------------ using relative delta module : to get difference in any part -----')
diff_parts = relativedelta.relativedelta(date_today,custom_date)
print(diff_parts)
print(diff_parts.years)
print(diff_parts.months)
print(diff_parts.days)

