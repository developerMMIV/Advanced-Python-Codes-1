count= ('Zero','One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
        'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty')
while True:
    num = int(input('Put your number:'))
    if 0<= num <= 21:
        break
        print('Try Again')
print(f'You choose number: {count[num]}')