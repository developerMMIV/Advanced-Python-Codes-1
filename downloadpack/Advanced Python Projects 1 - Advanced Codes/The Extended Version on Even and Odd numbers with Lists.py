num = [[], []]
value = 0
for r in range(1,7):
    value = int(input(f'Type the {r} number: '))
    if value%2==0:
        num[0].append(value)
    else:
        num[1].append(value)

num[0].sort()
num[1].sort()
print(f'The even numbers are {num[0]} and the odd {num[1]}')