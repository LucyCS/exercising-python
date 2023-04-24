name = str(input('Enter a phrase: '))
print("The letter A appears {} time.".format(name.strip().lower().count('a')))
print('The letter A appears for the first time at position {}.'.format(name.strip().lower().find('a') + 1))
print('The letter A appears for the last time at position {}.'.format(name.strip().lower().rfind('a') + 1))