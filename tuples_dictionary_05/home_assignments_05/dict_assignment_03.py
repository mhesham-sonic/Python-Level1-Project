print('---------------------Library example ----------------------')
book_dict = {'Pages': '277', 'Name': 'Gone_Girl', 'Year': 2007}
print(book_dict)

print('---------------------Adding new element ( author ) To a Dictionary----------------------')
book_dict['Author'] = 'David Fincher'
print(book_dict)

print('---------------------Accessing Elements ( name ) inside a Dictionary----------------------')
print(book_dict['Name'])

print('---------------------Changing Elements inside a Dictionary year to 2010----------------------')
book_dict['Year'] = 2010
print(book_dict)

print('---------------------Use Loop to print keys and values----------------------')
for key, value in book_dict.items():
    print(key, value)

print('---------------------Removing Item ( name ) from a Dictionary----------------------')
book_dict.pop('Name')
print(book_dict)
