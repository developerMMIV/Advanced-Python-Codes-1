list = ('Rice', 2.00,
        'Beans', 4.00,
        'Tomatoes', 2.50,
        'Biscuit', 1.50,
        'Potatoes', 2.00,
        'Wheat', 5.00,
        'Carrots', 3.00,)



for pos in range(0 ,len(list)):
    if pos %2 ==0:
        print(f'{list[pos]:.<30}',end='')
    else:
        print(f'${list[pos]:>7.2f}')
