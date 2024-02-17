numberoflists =[]
lar = 0
sma = 0
for c in range(0,5):
    numberoflists.append(int(input('Add your number:')))
    if c==0:
        lar = sma = numberoflists[c]
    else:
        if numberoflists[c] > lar:
            lar = numberoflists[c]
        if numberoflists[c] < sma:
            sma = numberoflists[c]
print(f'There are {numberoflists} ')
print(f'The largest number is {lar} while the smallest number is {sma} ')
