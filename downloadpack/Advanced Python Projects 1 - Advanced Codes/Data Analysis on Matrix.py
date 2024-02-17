matrix = [[0,0,0],[0,0,0],[0,0,0]]
spar=mai=scol=0
for r in range(0,3):
    for c in range(0,3):
        matrix[r][c]= int(input(f'Insert a number for {[r],[c]}:  '))

for r in range(0,3):
    for c in range(0,3):
        print(f'[{matrix[r][c]:^5}]',end=' ')
        if matrix[r][c]%2==0:
            spar+= matrix[r][c]
    print()
print(f'The sum of the even numbers are {spar}')

for l in range(0,3):
    scol+=matrix[l][2]
print(f'The sum of numbers in the third column are {scol}')
for c in range(0,3):
    if c==0:
        mai=matrix[1][c]
    elif matrix[1][c]>mai:
        mai = matrix[1][c]
print(f'The largest number in the third line is {mai}')