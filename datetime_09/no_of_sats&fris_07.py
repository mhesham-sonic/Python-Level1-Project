
from datetime import datetime
from dateutil import relativedelta

print('----------------Number of SAT and FRI in a given month')

input_date = datetime(day=1, month=6, year=2023)
end_date = input_date + relativedelta.relativedelta(months=1, day=1)
count_sat = 0
count_fri = 0

while input_date < end_date:
    if input_date.weekday() == 4:
        count_fri += 1
    elif input_date.weekday() == 5:
        count_sat += 1
    input_date = input_date + relativedelta.relativedelta(days=1)

print('Number of Fridays= ', count_fri)
print('Number of Saturdays= ', count_sat)
