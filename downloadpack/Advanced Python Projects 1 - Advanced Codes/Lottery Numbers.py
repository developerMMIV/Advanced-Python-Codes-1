from random import randint
from time import sleep
list = []
jogos = []


quant = int(input('How many games to you want ? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in list:
            list.append(num)
            cont+=1
        if cont>=6:
            break
    list.sort()
    jogos.append(list[:])
    list.clear()
    tot+=1
print('-='*30,)
for i, l in enumerate(jogos):
    print(f'Game{i+1}: {l}')
    sleep(1)
print('Good Luck')