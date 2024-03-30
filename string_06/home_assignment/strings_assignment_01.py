print('------------Count occurrences of a word in string------------')

str1 = 'A computer Science Portal for Portal'
str1 = str1.lower()
list1 = str1.split()
print(list1)
count_word = 0

for item in list1:
    if item == 'portal':
        count_word += 1

print('Number of Occurrence of Word Portal: ', count_word)



