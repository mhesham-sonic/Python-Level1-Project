print('---------------item with price and quantity------------')


def format_order(x,y,z):
    return print(f'This Order Contains:{x} ,price={y:.2f} $ ,quantity={z} plates')


item, price, quantity = ('Rice', 70000, 2)
format_order(item, price, quantity)

