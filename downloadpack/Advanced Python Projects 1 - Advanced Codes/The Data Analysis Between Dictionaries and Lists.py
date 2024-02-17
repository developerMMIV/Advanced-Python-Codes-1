guys = []
people = {}
sum = median = 0
while True:
    people.clear()
    people['nome'] = str(input('Name:'))
    while True:
        people['sex'] = str(input('Sex: [M/F] ')).upper()[0]
        if people['sex'] in 'MF':
            break
        print('ERROR! Please try again')
    people['age']= int(input('Age: '))
    sum += people['age']
    guys.append(people.copy())
    while True:
        resp =str(input('Want to continue? S/N:')).upper()[0]
        if resp in "SN" :
            break
        print('ERROR! Please try again')
    if resp == 'N':
        break

print()
print(f'A) Total of {len(guys)} registered people ')
median = sum/len(guys)
print(f'B) the age median: {median:5.2f} years')
print(f'C) Number of women',end=' ')
for p in guys:
    if p['sex'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print()
print(f'D) Number of people above the median ', end= ' ')
for p in guys:
    if p['age'] >= median:
        print(f'  ', end=' ')
        for k, v in p.items():
            print(f'{k}= {v};', end=' ')
        print()
print()
