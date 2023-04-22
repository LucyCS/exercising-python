km = float(input('Enter the total of KM driven: '))
days = int(input('Enter the number of days rented: '))

kmTotal = km * 0.15
daysTotal = days * 60

print('The total price to be paid is ${:.2f}'.format(kmTotal + daysTotal))