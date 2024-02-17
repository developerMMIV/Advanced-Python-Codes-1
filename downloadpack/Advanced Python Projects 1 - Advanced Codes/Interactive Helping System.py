from time import sleep
c = ('\033[m' ,              #0-No Colors
     '\033[0;30;41m' ,       #1-Red
     '\033[0;30;42m' ,       #2-Green
     '\033[0;30;43m',        #3-Yellow
     '\033[0;30;44m',        #4-Blue
     '\033[0;30;45m',        #5-Pulp
     '\033[7;30m'
     )     #6-White


def assist(com):
    title(f'Accessing the manual do command \'{com}\'', 4)
    print(c[6], end=' ')
    help(com)
    print(c[0], end=' ')
    sleep(2)
def title(msg,cor=0):
    tam = len(msg)+4
    print(c[cor],end=' ')
    print('~'*tam)
    print(f'{msg}')
    print('~'*tam)
    print(c[0],end='')
    sleep(1)


comando =' '
while True:
    title('SYSTEM OF HELP PyHELP', 2)
    comando = str(input("Function or Library> "))
    if comando.upper()=='END':
        break
    else:
        assist(comando)
title('TILL NEXT TIME', 1)