width = float(input('Enter wall width: '))
height = float(input('Enter wall height: '))

area = width * height

print('Its wall has dimension {:.2f} x {:.2f} and its area is {:.2f} m².'.format(width, height, area))
print('To paint this wall, you will need {:.2f} L of paint.'.format(area / 2))