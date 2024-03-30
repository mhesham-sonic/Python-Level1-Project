print('----------------from file to list with split words--------------')

with open('C:\\MY_FILES\\read_data.txt', 'r') as file:
    content = file.read()
    words_list = content.split()
    print(words_list)
