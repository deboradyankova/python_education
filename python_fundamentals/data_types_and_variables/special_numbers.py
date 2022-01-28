special_sums = [5, 7, 11]

n = int(input())

for number in range(1, n + 1):
   digits_sum = sum([int(dig) for dig in str(number)])
   if digits_sum in special_sums:
       print(f'{number} -> True')
   else:
       print(f'{number} -> False')


