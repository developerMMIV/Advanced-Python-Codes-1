digits = []
while True:
    digits.append(int(input('Insert your number:')))
    resp = str(input('Continue? Y/N'))
    if resp in 'Nn':
        break

print(f'You inserted {len(digits)} digits')
digits.sort(reverse=True)
print(f'The numbers in the countdown form: {digits}')
if 5 in digits:
    print('Number 5 is the member of the list ')
else:
    print('Number 5 is not on the list')