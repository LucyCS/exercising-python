import random

linha = '--=' * 20
print('''
{}\nI will think in a number between 0 and 5. Try to guess...\n{}
'''.format(linha, linha))
number = int(input('What number did I think of? '))
numberRandom = random.randint(0, 5)
if number == numberRandom:
    print('CONGRATULATIONS! You could beat me!')
else:
    print('I WON! I thought of the number {} and not {}.'.format(numberRandom, number))