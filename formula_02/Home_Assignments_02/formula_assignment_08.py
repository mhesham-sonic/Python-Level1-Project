import math

print('-----------program to calculate monthly payment------------')

loan_amount = int(input('Please Select loan_amount value = '))
monthly_interest_rate = float(input('Please Select monthly_interest_rate value = '))
no_of_years = int(input('Please Select no_of_years value = '))

part_01 = loan_amount * monthly_interest_rate
part_02 = math.pow((1 + monthly_interest_rate),(no_of_years * 12))
part_03 = 1 / part_02
monthly_payment = part_01 / (1 - part_03)
total_payment = monthly_payment * no_of_years * 12

print('Monthly Payment = ',monthly_payment)
print('Total Payment = ', total_payment)

