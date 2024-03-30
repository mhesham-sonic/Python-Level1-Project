print('----------------Identifying +ve & -ve & 0 in list---------------')
numbers_list = [15, -16, 20, -3, 0, 20]
no_pos_elements = 0
no_neg_elements = 0
no_zeros = 0
sum_pos_elements = 0
sum_neg_elements = 0

for item in numbers_list:
    if item > 0:
        no_pos_elements = no_pos_elements + 1
        sum_pos_elements = sum_pos_elements + item
    elif item < 0:
        no_neg_elements = no_neg_elements + 1
        sum_neg_elements = sum_neg_elements + item
    else:
        no_zeros = no_zeros + 1

print(numbers_list)
print('no_pos_elements:',no_pos_elements)
print('no_neg_elements:',no_neg_elements)
print('no_zeros:',no_zeros)
print('sum_pos_elements:',sum_pos_elements)
print('sum_neg_elements:',sum_neg_elements)
