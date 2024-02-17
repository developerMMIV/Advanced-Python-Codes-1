from random import randint

numbers = []
code = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))
ze =0
for read in range(0,5):
   numbers.append(int(input('Insert a number lesser than 10:')))


if numbers == code:
    print('ok')
else:
    print('incorrect')