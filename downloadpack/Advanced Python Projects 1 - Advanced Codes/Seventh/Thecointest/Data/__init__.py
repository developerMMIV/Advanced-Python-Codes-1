def readmoney(msg):
    valid = False
    while not valid:
        entrada = str(input(msg)).replace(',', '.')
        if entrada.isalpha() or entrada.strip() == '':
            print(f'\033[0;31mERROR \"{entrada}\" is a invalid price\033[m')
        else:
            valid = True
            return float(entrada)