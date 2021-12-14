start = int(input())
end = int(input())
magic_number = int(input())

combination_n = 0
combination_achieved = False
n_of_comb = 0

for n1 in range(start, end + 1):

    if combination_achieved:
        break

    for n2 in range(start, end + 1):
        combination_n += 1

        if n1 + n2 == magic_number:
            print(f'Combination N:{combination_n} ({n1} + {n2} = {magic_number})')
            combination_achieved = True
            break

if not combination_achieved:
    print(f'{combination_n} combinations - neither equals {magic_number}')
