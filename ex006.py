number = int(input('Enter an integer number: '))
double = number * 2
triple = number * 3
squareroot = number ** (1/2)
print('''Number = {}
Double = {}
Triple = {}
Square Root = {:.2f}
'''.format(number, double, triple, squareroot))