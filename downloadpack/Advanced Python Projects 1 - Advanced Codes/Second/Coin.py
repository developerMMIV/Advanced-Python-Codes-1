def Increase(price=0, tax=0):
    res = price + (price*tax/100)
    return res
def Decrease(price=0,tax=0):
    res = price - (price*tax/100)
    return res
def Double(price=0):
    res = price*2
    return res
def Half(price=0):
    res = price/2
    return res

def Penny(price=0, coin='$'):
    return f'{coin}{price:>.2f}'.replace('.',',')