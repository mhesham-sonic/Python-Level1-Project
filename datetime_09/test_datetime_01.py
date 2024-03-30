
from datetime import datetime  # from module datetime import class datetime

# Here we will show all basic operations on datetime

print('---- Get the current date and time -----')

date_today = datetime.now()
print(date_today)

print('---- get only date or time or their parts -------')

print(date_today.date())
print(date_today.year)
print(date_today.month)
print(date_today.day)
print(date_today.weekday())  # Mon = 0

################

print(date_today.time())
print(date_today.hour)
print(date_today.minute)
print(date_today.second)



print('---- Re Formatting date, time --- | we use strftime() function----')
print('----- Convert date into string using strftime() function -----')
# day, month, year,yr,weekday, week no per Year
print(date_today.strftime('%d-%m-%Y %y %w %W'))

# Month, Mon, Day, Dy
print(date_today.strftime('%B-%b-%A-%a'))

# Hours in 24 hours style
print(date_today.strftime('%H:%M:%S'))

# Hours in 12 hours style
print(date_today.strftime('%I:%M:%S %p'))

print('---------------- Create a custom date : 24-04-2023 ------------')
print('-- 1st way : datetime object using constructor ( ) ')
custom_date = datetime(year=2023, month=4, day=24)
print(custom_date)

print('--- 2nd way - by converting a string to Date using strptime() function -----')
my_date_str = '10-3-2024'
new_custom_date = datetime.strptime(my_date_str, '%d-%m-%Y')
print(new_custom_date)



print('----------- Comparison ------------')

if date_today.date() > custom_date.date():
    print(date_today, ' is after ', custom_date)
elif date_today.date() < custom_date.date():
    print(date_today, ' is before ', custom_date)
else:
    print(date_today, ' is equal to ', custom_date)