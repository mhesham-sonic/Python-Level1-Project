print('------------------program to calculate order discount based on conditional if--------')

item_cost = float(input('Please Enter Item Cost : '))
item_qty = int(input('Please Enter Item Quantity : '))
special_client = int(input('Please Confirm if Special Client or not : '))

total_order_cost = item_cost * item_qty

if total_order_cost >= 1000:
    if special_client != 0:
        print('This Client is Special')
        discount_pct = 0.2
    else:
        print('This Client is Not Special')
        discount_pct = 0.1
else:
    print('No Discount')
    discount_pct = 0

discount_val = discount_pct * total_order_cost
total_cost_with_discount = total_order_cost - discount_val

print('Discount Percentage = ' + str(discount_pct * 100) + '%')
print('Discount Value = ',discount_val)
print('Total Order Cost Before Discount = ',total_order_cost)
print('Total Order Cost After Discount = ',total_cost_with_discount)