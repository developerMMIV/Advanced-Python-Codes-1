from datetime import datetime
data = {}
data["Name"] = str(input('What is your name?:'))
nasc = int(input('Year of Birth:'))
data["Age"] = datetime.now().year - nasc
data["CTPS"]= int(input('Worker Card Number:(0 if you dont have):'))
if data != 0:
    data["Contract"]= int(input("Year of contract:"))
    data["Salary"]= float(input("Salary: $"))
    data["Retirement"]= data["Age"]+  (data["Contract"]+ 35 - datetime.now().year)

for v, n in data.items():
    print(f'- {v}  is {n}')