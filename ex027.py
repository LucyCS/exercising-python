name = str(input('Enter your full name: '))
print('''Nice to meet you!
Your first name is {}.
Your last name is {}.'''.format(name.split()[0],name.split()[len(name.split()) - 1])
    )