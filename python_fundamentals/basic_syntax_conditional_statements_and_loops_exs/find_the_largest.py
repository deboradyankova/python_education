from itertools import permutations

number = list(input())

number_perm = permutations(number)
max_number = max([int(''.join(list(x))) for x in number_perm])

# max_number = int(''.join(number))

# for n in list(number_perm):
#     n = int(''.join(list(n)))
#     if n > max_number:
#         max_number = n
#
print(max_number)
