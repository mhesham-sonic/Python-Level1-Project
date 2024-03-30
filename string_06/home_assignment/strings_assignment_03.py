print('---------Make Uppercase Half String-----------------')

str1 = 'ArabRepublicOfEgypt'
list1 = []

for i in range(len(str1)):
    list1.append(str1[i])

half_size = (len(list1) - 1) / 2
X = int(half_size)

for j in range((X + 1)):
    list1[j] = list1[j].lower()

for z in range(X, len(list1)):
    list1[z] = list1[z].upper()

str2 = ''.join(list1)

print('Original String = ', str1)
print('Converted String = ', str2)

