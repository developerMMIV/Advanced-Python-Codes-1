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