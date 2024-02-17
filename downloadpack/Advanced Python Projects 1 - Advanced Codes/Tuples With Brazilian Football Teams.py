team = ('Palmeiras', 'Gremio', 'Atletico- MG','Flamengo','Botafogo', 'Bragantino','Fluminense','Athletico-PR',
       'Internacional', 'Fortaleza', 'São Paulo', 'Cuiaba', 'Corinthians','Cruzeiro','Vasco','Bahia','Santos',
        'Goias', 'Coritiba' , 'America-MG')

print(f'List of teams in Brasilerão:{team}')
print(f'The first 5 teams{team[0:5]}')
print(f'The last four teams {team[-4:]}')
print(f'In the alphabet order {sorted(team)}')
print(f'And the position where Corinthians is: {team.index("Corinthians")+1} position')