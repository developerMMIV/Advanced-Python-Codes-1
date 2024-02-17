import Coin

p = float(input('Type the price $'))
print(f'The half of {Coin.Penny(p)} is {Coin.Half(p,True)}')
print(f'The double of {Coin.Penny(p)} is {Coin.Double(p,True)}')
print(f'If we increase 10% it will be {Coin.Increase(p , 10, True)}')
print(f'And decreased {Coin.Decrease(p , 10,True)}')
