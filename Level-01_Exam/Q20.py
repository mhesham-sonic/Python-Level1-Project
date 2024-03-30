print('---------Occurrence of word in string without built in function------------')


def count_word(str1, word1):
    list1 = str1.split(' ')
    count = 0
    for item in list1:
        if item == word1:
            count += 1
    return count


input_string = 'I love Math & Physics & Engineering & Network & Math & IP & Math'
word_check = 'Math'
print('No. of Occurrence of word: ',word_check, ' is ', count_word(input_string,word_check))