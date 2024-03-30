print('----------- basic operations for dictionary --------------')

print('---- create and print dictionary -----')
shopping_cart_prices = {'Milk': 40.0,'Eggs': 180.0,'Bread': 10.0}
print(shopping_cart_prices)
print(type(shopping_cart_prices))

print('------ Adding, change new pair to the dictionary -------')
shopping_cart_prices['Nescafe'] = 55.0
print(shopping_cart_prices)
shopping_cart_prices['Milk'] = shopping_cart_prices['Milk'] + 5
print(shopping_cart_prices)

print('------ access element -----')
print(shopping_cart_prices['Milk'])


print('---- delete element pair from dict ------')
shopping_cart_prices.pop('Nescafe')
print(shopping_cart_prices)
