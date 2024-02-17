team = []
player = {}
rounds =[]

while True:
    player.clear()
    player['name']= str(input('Name of the player:'))
    tot = int(input(f'How many rounds did {player["name"]} played?'))
    for c in range (0, tot):
        rounds.append(int(input(f'How many goals in round {c+1}? ')))
    player['Goals']= rounds[:]
    player['Total']= sum(rounds)
    team.append(player.copy())
    while True:
        resp = str(input('Continue? Y/N')).upper()[0]
        if resp in 'YN':
            break
        print('ERROR! Try Again')
    if resp == 'N':
        break
print('-='*30)
print('cod', end='')
for i in  player.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(team):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)