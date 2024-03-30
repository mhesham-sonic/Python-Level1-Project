import sys

print('------------------Dict Key not Found----------------')


def fetch_element(dictionary1, c):
    try:
        val_01 = dictionary1[c]
    except KeyError:
        print('Key not found in the dictionary!')
        sys.exit()
    return val_01


dict1 = {'a': 1, 'b': 2}
print('Key', 'has Value: ', fetch_element(dict1,'c'))

