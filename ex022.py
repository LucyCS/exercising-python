name = str(input('Enter your name complete: '))

print('Analysing your name...')
print('Your name in upper case is {}.'.format(name.upper()))
print('Your name in lower case is {}.'.format(name.lower()))
print('Your name have {} letters.'.format(len(name.replace(' ', ''))))
print('Your first name is {} and it has {} letters.'.format(name.split()[0], len(name.split()[0])))