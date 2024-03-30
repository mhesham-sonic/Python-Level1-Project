from datetime import datetime
from dateutil import relativedelta
print('---------------program checks if a specific date falls between two provided dates-----------')

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)
given_date = datetime(2023, 6, 15)

if start_date <= given_date <= end_date:
    print('The given date is in range')
else:
    print('The given date is outside the range')
