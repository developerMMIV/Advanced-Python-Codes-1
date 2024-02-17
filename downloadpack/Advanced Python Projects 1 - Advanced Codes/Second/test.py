import Coin

p = float(input('Type the price $'))
print(f'The half of {Coin.Penny(p)} is {Coin.Penny(Coin.Half(p))}')
print(f'The double of {Coin.Penny(p)} is {Coin.Penny(Coin.Double(p))}')
print(f'If we increase 10% it will be {Coin.Penny(Coin.Increase(p , 10))}')
print(f'And decreased ${Coin.Decrease(p , 10)}')
