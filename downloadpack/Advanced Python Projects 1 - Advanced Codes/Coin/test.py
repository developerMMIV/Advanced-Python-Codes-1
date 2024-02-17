import Coin

p = float(input('Type the price $'))
print(f'The half of ${p} is ${Coin.Half(p)}')
print(f'The double of ${p} is ${Coin.Double(p)}')
print(f'If we increase  it will be ${Coin.Increase(p , 10)}')
print(f'And decreased ${Coin.Decrease(p , 10)}')
