print('--------- Nested List -----------')
my_nested_list = [
        [101, 'ahmed', 'Cairo'],
        [102, 'mostafa', 'Alex']
]
print(my_nested_list)
print(my_nested_list[0])    # [101, 'ahmed', 'Cairo']
print(my_nested_list[1]) # [102, 'mostafa', 'Alex'
print(my_nested_list[0][2]) # Cairo

print('----------------------------')
my_nested_list = [
        [101, 'ahmed', 'Cairo'],
        [102, 'mostafa', 'Alex'],
        [103, 'ibrahim', [11288, 'Nasr city', 'Makram Ebeid street']]
]
print(my_nested_list[2][2][2])