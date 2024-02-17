num = []
even = []
odd = []
while True:
    num.append(int(input('Insert Your number:')))
    resp = str(input('Continue? Y/N '))
    if resp in 'Nn':
        break

for i,v in enumerate(num):
    if v%2==0:
        even.append(v)
    else:
        odd.append(v)
print(f'This are the complete numbers {num}')
print(f'The odd numbers {odd} and the even {even}')