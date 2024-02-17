from random import randint
from time import sleep
from operator import itemgetter
game = {'Player 1' : randint(1,6),
        'Player 2' : randint(1,6),
        'Player 3' : randint(1, 6),
        'Player 4' : randint(1,6)}
ranking =[]
print('Game Value')
for k,v in game.items():
    print(f'{k} scored:{v}')
    sleep(1)
ranking= sorted(game.items(), key=itemgetter(1),reverse=True)
print('RANKING')
for v, t in enumerate(ranking):
    print(f'The {v+1} postion: {t[0]}')
    sleep(1)