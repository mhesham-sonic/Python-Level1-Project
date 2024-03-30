print('---------------operations on list of dictionaries----------------')

data_list = [{101: 'Farouk', 102: 'Mostafa', 103: 'Marwa'}]
print(data_list)
print(data_list[0])
print(data_list[0][103])
data_list[0][103] = 'Marwa Mohamed'
print(data_list)
dict1 = data_list[0]
dict2 = {}
dict2[104] = 'Ibrahim'
dict2[105] = 'Sanaa'
data_list.append(dict2)
#dict1.update(dict2)
print(dict1)
# data_list = [dict1,dict2]
print(data_list)
print(data_list[1][105])

