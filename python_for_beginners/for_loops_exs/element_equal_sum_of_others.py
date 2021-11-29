from sys import maxsize

loop = int(input('n'))

result = 0
max_number = -maxsize

for i in range(loop):
    number = int(input())
    result += number

    if number > max_number:
        max_number = number
result -= max_number
if max_number == result:
    print(f'Yes sum = {max_number}')

else:
    print(f'No Diff = {abs(max_number - result)}')


