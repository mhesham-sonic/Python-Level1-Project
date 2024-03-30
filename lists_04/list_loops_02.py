print('--------------------loops on list using for index loop ( for i loop ) ----------------')

numbers_list = [1, 7, 23, 60, 85, 10]
sum_elements = 0
max_elements = numbers_list[0]
min_elements = numbers_list[0]
for i in range(len(numbers_list)):
    print(numbers_list[i])
    sum_elements = sum_elements + numbers_list[i]
    if numbers_list[i] > max_elements:
        max_elements = numbers_list[i]

    if numbers_list[i] < min_elements:
        min_elements = numbers_list[i]

print('Sum of Elements= :', sum_elements)
print('max between elements : ', max_elements)
print('min between elements : ', min_elements)

print(sum(numbers_list))
print(max(numbers_list))
print(min(numbers_list))

print('--------------------loops on list using for each loop ( for in loop ) ----------------')
sum_elements = 0        # reset variable
for item in numbers_list:
    print(item)
    sum_elements = sum_elements + item

print('Sum of Elements =',sum_elements)

