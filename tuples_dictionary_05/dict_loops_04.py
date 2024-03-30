print('------- Loop over dictionary using for each loop : loop over all keys ----------------')
shopping_cart_prices = {'Milk': 40.0,'Eggs': 180.0,'Bread': 10.0}
for key in shopping_cart_prices:
    print(key, shopping_cart_prices[key])

print('-------Loop over dictionary using for each loop : loop over all keys | values -----')
for key, value in shopping_cart_prices.items():
    print(key, value)
