n = int(input())

left_sum = 0
right_sum = 0

for i in range(n):

    first_num = int(input())
    sec_num = int(input())

    if i % 2 == 0:
        left_sum = first_num + sec_num
    else:
        right_sum = first_num + sec_num
        if left_sum == right_sum:
            print(f'Yes, sum = {right_sum}')
        else:
            print(f'No, diff = {abs(right_sum - left_sum)}')
        left_sum = 0
        right_sum = 0
