from random import randint
numbers = (randint(1,10),randint(1,10),randint(1,10),randint(1,10)
           ,randint(1,10))
print('The chosen numbers are:', end= ' ')
for n in numbers:
    print(n, end=' ')
print(f'\nThe highest number chosen is {max(numbers)}')
print(f'And the lowest: {min(numbers)}')