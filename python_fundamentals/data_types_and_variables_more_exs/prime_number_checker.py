number = int(input())

is_prime = True

if number > 1:
    for n in range(2, number // 2):
        if number % n == 0:
            is_prime = False
            print('False')
            break
else:
    raise InputError('Not correct input of number')

if is_prime:
    print('True')