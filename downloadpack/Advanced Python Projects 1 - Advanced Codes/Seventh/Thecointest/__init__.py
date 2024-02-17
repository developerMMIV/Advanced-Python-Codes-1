def readmoney(msg):
     valid = False
     while not valid:
         entrada =str(input(msg))
         if entrada.isalpha():
            print(f'ERROR\"{entrada}\" is a invalid price')
         else:
            valid=True
            return float(entrada)