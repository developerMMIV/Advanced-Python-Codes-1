def ficha(play='<unknown>', goals=0):
  if g > 1:
    print(f'The player {play} made {goals} goals in the league')
  else:
      print(f'The player {play} made {goals} goal in the league')

n = str(input('Name of the player:'))
g = str(input('Number of goals the player scored:'))
if g.isnumeric():
    g = int(g)
else:
    g =0
if n.strip() == '':
    ficha(goals=g)
else:
    ficha(n,g)
