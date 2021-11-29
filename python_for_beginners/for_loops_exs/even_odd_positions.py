from sys import maxsize

loop = int(input('loop'))

odd_max = -maxsize
odd_min = maxsize
even_max = -maxsize
even_min = maxsize

odd_sum = 0
even_sum = 0

for i in range(1, loop + 1):

    number = float(input())

    if i % 2 == 0:
        even_sum += number
        if number > even_max:
            even_max = number
        if number < even_min:
            even_min = number
    else:
        odd_sum += number
        if number > odd_max:
            odd_max = number
        if number < odd_min:
            odd_min = number

if loop == 1:
    print(f'OddSum={odd_sum:.2f},\n'
          f'OddMin={odd_min:.2f},\n'
          f'OddMax={odd_max:.2f},\n'
          f'EvenSum={even_sum:.2f},\n'
          f'EvenMin=No,\n'
          f'EvenMax=No,'
          )
elif loop > 1:
    print(f'OddSum={odd_sum:.2f},\n'
          f'OddMin={odd_min:.2f},\n'
          f'OddMax={odd_max:.2f}\n'
          f'EvenSum={even_sum:.2f},\n'
          f'EvenMin={even_min:.2f},\n'
          f'EvenMax={even_max:.2f},'
          )
else:
    print('OddSum=0.00,\n'
          'OddMin=No,\n'
          'OddMax=No,\n'
          'EvenSum=0.00,\n'
          'EvenMin=No,\n'
          'EvenMax=No'
          )
