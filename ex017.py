import math

opposite = float(input('Enter the opposite leg: '))
adjacent = float(input('Enter the adjacent leg: '))

hypotenuse = math.sqrt(opposite * opposite + adjacent * adjacent)

print('The hypotenuse of this triangle is: {:.2f}.'.format(hypotenuse))