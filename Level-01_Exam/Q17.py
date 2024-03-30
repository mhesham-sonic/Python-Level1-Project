print('----------changing pricing list--------------')

sum_items = 0
raise_val = 0.1
vat_val = 0.14
shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}

for key,value in shopping_cart_dict.items():
    shopping_cart_dict[key] = value + (value * 0.1)
    sum_items = sum_items + shopping_cart_dict[key]
print(sum_items)

net_value = sum_items + (sum_items * 0.14)

print('shopping cart after 10% raise = ', shopping_cart_dict)
print('Net Value after 14% VAT= ', net_value)
