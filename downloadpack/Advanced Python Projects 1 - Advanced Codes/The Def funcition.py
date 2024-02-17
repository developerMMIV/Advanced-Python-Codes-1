from time import sleep
def maior(* num):
    cont = maior = 0
    print(f'\nChecking the numbers..... ')
    for value in num:
        print(f'{value}', end=' ',flush=True)
        sleep(0.3)
        if cont == 0:
            maior = value
        else:
            if value > maior:
                maior = value
        cont += 1
    print(f'It was informed {cont} numbers in the board')
    print(f'And the biggest value is {maior}')


maior(1,2,3,4,5,6,7)
maior(8,9,0,11,12)
maior(5,8,9,0,2)
maior(4,3,5,4)
maior(3,12,56)
maior()


