import random

stu1 = str(input('First student: '))
stu2 = str(input('Second student: '))
stu3 = str(input('Third student: '))
stu4 = str(input('Fourth student: '))

list = [stu1, stu2, stu3, stu4]


random.shuffle(list)
print('The order of presentation will be\n' 
      + str(list))