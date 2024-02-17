def Increase(price=0, tax=0, formato=False):
    res = int(price + (price*tax/100))
    return res if  formato is False else Penny(res)
def Decrease(price=0,tax=0, formato=False):
    res = int(price - (price*tax/100))
    return res if  formato is False else Penny(res)
def Double(price=0, formato=False):
    res = price*2
    return res if formato is False else Penny(res)
def Half(price=0, formato=False):
    res = int(price/2)
    return res if formato is False else Penny(res)

def Penny(price=0, coin='$'):
    return f'{coin}{price:>.2f}'.replace('.',',')

def Resume(price=0,taxee=10,taxer=6):
    print('Price Resumt')
    print('~'*30)
    print(f'Analyised Price: \t{Penny(price)}')
    print(f'Price Double:     \t{Double(price,True)}')
    print(f'Half of the Price: \t{Half(price,True)}')
    print(f'With {taxee}% increase: \t{Increase(price,taxee,True)}')
    print(f'With {taxer}% decrease: \t{Decrease(price,taxer,True)}' )
    print('~'*30)