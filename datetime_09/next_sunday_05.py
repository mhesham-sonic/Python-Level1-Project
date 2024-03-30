import calendar
from datetime import datetime  # from module datetime import class datetime
from dateutil import relativedelta  # from package dateutil import module relativedelta


print('-----------------Get Next wednesday------------------')

date_today = datetime.now()
#target_date = date_today + relativedelta.relativedelta(weekday=2)  #method1
target_date = date_today + relativedelta.relativedelta(weekday=calendar.WEDNESDAY) #method2
print(target_date)

print('-----------------Get Next 2 wednesday------------------')
target_date2 = date_today + relativedelta.relativedelta(weekday=calendar.WEDNESDAY , weeks=1)
print(target_date2)

print('-----------------Get 1st wednesday in this current month------------------')
target_date3 = date_today + relativedelta.relativedelta(day=1,weekday=calendar.WEDNESDAY)
print(target_date3)

print('-----------------Get 1st wednesday in this next month------------------')
target_date4 = date_today + relativedelta.relativedelta(months=1,day=1,weekday=calendar.WEDNESDAY)
print(target_date4)

print('-----------------Get 1st wednesday in this current year ------------------')
target_date5 = date_today + relativedelta.relativedelta(month=1,day=1,weekday=calendar.WEDNESDAY)
print(target_date5)

print('-----------------Get 1st wednesday in this next year ------------------')
target_date6 = date_today + relativedelta.relativedelta(years=1,month=1,day=1,weekday=calendar.WEDNESDAY)
print(target_date6)