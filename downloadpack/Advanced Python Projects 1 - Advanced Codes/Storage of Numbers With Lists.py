numbers = []
while True:
    n = int(input('Insert Your number:'))
    if n not in numbers:
        numbers.append(n)
        print('Number stored successfully')
    else:
        print('Already stored this number, try again')
    a = str(input('Continue? Y/N '))
    if a in 'Nn':
        break
print('-=-'*25)
numbers.sort()
print(f'You stored the numbers {numbers}')