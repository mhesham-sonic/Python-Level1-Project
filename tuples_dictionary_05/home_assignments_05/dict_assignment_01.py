print('------------------------Converting a List of Tuples to a Dictionary -----------------')

colours_list = [('red', 223), ('blue', 201), ('green', 210)]
dict_colour = {}
for i in range(len(colours_list)):
    colour = colours_list[i][0]
    value = colours_list[i][1]
    dict_colour[colour] = value
print(dict_colour)

dict2 = dict(colours_list) # This dict function ( Constructor - OOP ) works if list contains tuples only
print(dict2)