print('-----------------Remove all special characters except letters and numbers-------------')

str1 = '123abcjw:, .@! eiw'
str2 = ''
for letter in str1:
    if letter.isalnum():
        str2 = str2 + letter

print(str2)
