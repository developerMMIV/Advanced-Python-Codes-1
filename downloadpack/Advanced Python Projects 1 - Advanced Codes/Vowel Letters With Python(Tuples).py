words = ('life','food', 'new', 'old','young','instead',
         'solo','alone','new')
for w in words:
    print(f'\nin the word {w.upper()} we have:', end=' ')
    for letter in w:
        if letter.lower() in 'aeiou':
            print(letter, end=' ')
    