expr = str(input("What is your expression?:"))
pile = []

for ver in expr:
    if ver == "(":
        pile.append('(')
    elif ver == ')':
        if len(pile)>0:
            pile.pop()
        else:
            pile.append(')')
            break

if len(pile)==0:
    print('It is correct')
else:
    print('it is invalid')
