v = float(input('What is the current speed of the car? '))
limit = 80.0
if v <= limit:
    print('Have a nice day! Drive safely!')
else:
    print('''FINED! You have exceeded the allowed limit of 80!
You must pay a fine of R${:.2f}!
Have a nice day! Drive safely!'''.format((v - limit) * 7))