matrix = [[0,0,0],[0,0,0],[0,0,0]]
for r in range(0,3):
    for c in range(0,3):
        matrix[r][c]= int(input(f'Insert a number for {[r],[c]}:  '))

for r in range(0,3):
    for c in range(0,3):
        print(f'[{matrix[r][c]:^5}]',end=' ')
    print()