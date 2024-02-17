temp = []
princ = []
lar = sma = 0

while True:
    temp.append(str(input('Name:')))
    temp.append(str(input('Weight:')))
    if len(princ)==0:
        lar =sma=temp[1]
    else:
        if temp[1]>lar:
            lar = temp[1]
        if temp[1]<sma:
            sma=temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Continue? Y/N '))
    if resp in 'Nn':
        break

print(f'Total of people registered: {len(princ)} people')
print(f'The people with the highest weight registered: {lar} ',end=' ')
for p in princ:
    if p[1]==lar:
        print(f'[{p[0]}]',end=' ')
print()
print(f'The people with the lowest weight: {sma}', end=' ')
for p in princ:
    if p[1]==sma:
        print(f'[{p[0]}]', end=' ')
print()