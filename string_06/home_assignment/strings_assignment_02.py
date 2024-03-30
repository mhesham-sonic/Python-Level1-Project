print('-------------capitalize the first and last letters of each word in a given string.--------')

str1 = 'python exercises practise solution'
str1 = str1.title()
print(str1)
list1 = str1.split()
list2 = []
print(list1)

for i in range(len(list1)):
    list1[i] = list1[i][0:-1] + list1[i][-1].swapcase()

print(list1)





