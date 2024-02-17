def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok= True
        else:
            print('\033[0;31mError add a valid number\033[m')
        if ok:
            break
    return valor

n = leiaInt('Digit a number:')
print(f'You added the number {n}')