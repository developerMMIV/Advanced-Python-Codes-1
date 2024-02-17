fix = []
while True:
    name = str(input('Name:'))
    score1 = float(input('The first score:'))
    score2 = float(input('The second score'))
    media=(score1/score2)
    fix.append([name,[score1,score2],media])
    resp = str(input('Continue? Y/N'))
    if resp in 'Nn':
        break
for i, a in enumerate(fix):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*40)
    opc = int(input('Show which score of the student?(Press 1000 to stop):'))
    if opc == 1000:
        print('Ending.....')
        break
    if opc <= len(fix) -1:
        print(f'Score of {fix[opc][0]} is {fix[opc][1]}')
print('Thank you ')