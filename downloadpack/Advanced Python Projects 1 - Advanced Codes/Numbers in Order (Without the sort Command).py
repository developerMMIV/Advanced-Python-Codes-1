list = []
for c in range(0,6):
    n = int(input('Put your number:'))
    if c == 0 or n > list[-1]:
        list.append(n)
        print('------')
    else:
        pos = 0
        while pos < len(list):
            if n <= list[pos]:
                list.insert(pos,n)
                print('-----')
                break
            pos+=1

print(f'The numbers you inserted is {list} ')