value = input('Enter something: ')
print('Primitive type: {}'.format(type(value)))
print('Is blank? {}'.format(value.isspace()))
print('Is a number? {}'.format(value.isnumeric()))
print('Is alphabetic? {}'.format(value.isalpha()))
print('Is alphanumeric? {}'.format(value.isalnum()))
print('Is upper case? {}'.format(value.isupper()))
print('Is lower case? {}'.format(value.islower()))
print('Is capitalized? {}'.format(value.istitle()))