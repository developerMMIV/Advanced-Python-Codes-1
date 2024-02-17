player = {}
rounds =[]
player['name']= str(input('Name of the player:'))
tot = int(input(f'How many rounds did {player["name"]} played?'))
for c in range (0, tot):
    rounds.append(int(input(f'How many goals in round {c+1}? ')))
player['Goals']= rounds[:]
player['Total']= sum(rounds)
print()
print(player)
print()
for k, v in player.items():
    print(f'The camp {k} has the value {v}')
print('-='*30)
print(f'The Player {player["name"]} played {len(player["Goals"])} rounds')
for i, v in enumerate(player['Goals']):
    print(f'  => in the game {i}, made {v} goals.')
print(f'Total of {player["Total"]} goals')
