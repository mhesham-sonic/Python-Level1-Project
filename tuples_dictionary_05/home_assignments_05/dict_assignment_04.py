print('------------loop over all keys and raise the prices 10%--------------')

shopping_cart_dict = {'milk': 20.0, 'bread': 10.0, 'eggs': 145.0}
raise_ratio = float(input('Please enter Raise ratio in %:'))
vat_ratio = float(input('Please enter VAT ratio in %:'))
raise_value = raise_ratio / 100
vat_value = vat_ratio / 100
total = 0
for key, value in shopping_cart_dict.items():
    shopping_cart_dict[key] = shopping_cart_dict[key] + shopping_cart_dict[key] * raise_value

print('Shopping Cart after VAT= ', shopping_cart_dict)

for key, value in shopping_cart_dict.items():
    total = total + shopping_cart_dict[key]

total = total + total * vat_value
print('Total Value after vat= ', total)
