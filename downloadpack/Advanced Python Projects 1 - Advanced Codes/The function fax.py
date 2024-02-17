from time import sleep
from random  import  randint


def luckynum(lista):
    print('Chossing 5 values in the list', end=' ')
    for cont in range(0, 5):
        n = randint(1,10)
        lista.append(n)
        print(f'{n}', end=' ', flush= True)
        sleep(0.3)
    print('Ready')


def somapar(lista):
    sum = 0
    for value in lista:
        if value % 2 == 0:
            sum += value
    print(f'Suming the even values of {lista} we have {sum}')


numbers= list()
luckynum(numbers)
somapar(numbers)









numbers = list()