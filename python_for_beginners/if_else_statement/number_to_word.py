numbers_to_word = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

a = int(input('Number: '))

if a in numbers_to_word.keys():
    print(numbers_to_word[a])
else:
    print('number too big')
