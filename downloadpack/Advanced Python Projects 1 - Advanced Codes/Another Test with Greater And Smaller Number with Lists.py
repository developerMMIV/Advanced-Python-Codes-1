list = []
lar = 0
sma = 0
for c in  range(0,5):
    list.append(int(input('Insert your number:')))
    if c == 0:
        lar = sma = list[c]
    else:
        if list[c]> lar:
            lar = list[c]
        if list[c]< sma:
            sma = list[c]
print(f'The Numbers: {list}')
print(f'The Largest number is {lar} and the smalllest is {sma}')