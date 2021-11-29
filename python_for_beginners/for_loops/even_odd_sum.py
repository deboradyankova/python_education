loop = int(input())
odd_sum = 0
even_sum = 0

for i in range(1, loop + 1):

    first_numb = int(input())

    if i % 2 == 0:
        even_sum += first_numb
    else:
        odd_sum += first_numb

if odd_sum == even_sum:
    print('Yes')
    print(f'sum =  {odd_sum}')
else:
    print('No')
    print(f'Diff = {abs(odd_sum - even_sum)}')


