print('---------------numbers which are divisible by 7 and 5, between 1500 and 2700---------')

list1 = []

for i in range(1500,2701):
    if i % 5 == 0 and i % 7 == 0:
        list1.append(i)

print(list1)

