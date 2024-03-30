from datetime import datetime
from dateutil import relativedelta
print('-------------------get fall date in which range---------------------')

dates_list = [
    (datetime(2023, 1, 1), datetime(2023, 1, 10)),
    (datetime(2023, 1, 15), datetime(2023, 1, 20)),
    (datetime(2023, 2, 5), datetime(2023, 2, 15))
]
given_date = datetime(2023, 4, 19)
check = False
for i in range(len(dates_list)):
    if given_date >= dates_list[i][0] and given_date <= dates_list[i][1]: # if my_date[0] <= given_date <= my_date[1]
        check = True
        print('This Date falls between: ', dates_list[i][0], 'and ', dates_list[i][1])
if not check:
    print('Not Found')
