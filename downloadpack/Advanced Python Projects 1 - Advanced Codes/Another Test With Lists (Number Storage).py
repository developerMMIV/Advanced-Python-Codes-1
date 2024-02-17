numbers = []
while True:
    n = int(input('Insert your number:'))
    if n not in numbers:
        numbers.append(n)
        print('Number Stored Succesfully')
    else:
        print('Number Stored already,Try Again')

    s = str(input('Continue? Y/N '))
    if s in 'Nn':
        break

print('-=-'*40)
numbers.sort()
print(f'The numbers you stored is {numbers}')