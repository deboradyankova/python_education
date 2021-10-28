ONE_DIGIT_NUMS = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    0: '',
}
tens = {
    2: 'Twenty',
    3: 'Thirty',
    4: 'Forty',
    5: 'Fifty',
    6: 'Sixty',
    7: 'Seventy',
    8: 'Eighty',
    9: 'Ninety',
}
eleven_to_nineteen = {
    1: 'Eleven',
    2: 'Twelve',
    3: 'Thirteen',
    4: 'Fourteen',
    5: 'Fifteen',
    6: 'Sixteen',
    7: 'Seventeen',
    8: 'Eighteen',
    9: 'Nineteen',
}
number = input()


if len(number) == 1:
    print(ONE_DIGIT_NUMS[int(number)])
elif len(number) == 2 and int(number[0]) == 1:
    if int(number) == 10:
        print('ten')
    else:
        sec_dig = int(number[1])
        print(f'{eleven_to_nineteen[int(sec_dig)]}')
elif len(number) == 2:
    print(f'{tens[int(number[0])]} {ONE_DIGIT_NUMS[int(number[1])]}')
elif len(number) == 3:
    print('one hundred')
