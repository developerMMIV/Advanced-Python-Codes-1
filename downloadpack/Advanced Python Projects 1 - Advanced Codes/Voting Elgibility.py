def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual-ano
    if idade < 16:
        return f'With {idade} the vote is not valid'
    elif 16 <= idade < 18 or idade > 65:
        return f'With {idade} the vote is not mandatory'
    else:
        return  f'With {idade} your vote is mandatory'
nasc = int(input("Which Year were you born?"))
print(voto(nasc))
