num = (int(input('Insert a number:')),
       int(input('Insert another number:')),
       int(input('Insert another number:')),
       int(input('Insert another number:')),
       int(input('Insert another number:'))
       )
print(f'You pressed the digits: {num}')
print(f'You pressed the number 9: {num.count(9)} times')
if 3 in num:
    print(f'The number 3 is the {num.index(3)+1} position')
else:
    print('the number 3 is not seen in any position')
print('The even numbers shown are :',end=' ')
for n in num:
    if n % 2 ==0:
        print(n, end= ' ')