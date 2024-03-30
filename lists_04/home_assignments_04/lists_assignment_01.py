print('---------------count even & odd numbers in list with their sum-----------------')

numbers_list = [15, 16, 20, 3, 9, 20]
even_no_count = 0
odd_no_count = 0
even_sum = 0
odd_sum = 0

for item in numbers_list:
    if item % 2 == 0:
        print(item,' is Even Number')
        even_no_count = even_no_count + 1
        even_sum = even_sum + item
    else:
        print(item, ' is Odd Number')
        odd_no_count = odd_no_count +1
        odd_sum = odd_sum + item

print('Number of Even Items= ',even_no_count)
print('Number of Odd Items= ',odd_no_count)
print('Sum of Even Items= ',even_sum)
print('Sum of Odd Items= ',odd_sum)
