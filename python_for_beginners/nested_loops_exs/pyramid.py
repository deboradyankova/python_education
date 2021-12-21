n = int(input())
current_number = 1
finished = False

for x in range(1, n + 1):
    if finished:
        break
    row_result = ''

    for y in range(x):

        if current_number == n:
            row_result += str(current_number) + ' '
            print(row_result)
            finished = True
            break

        row_result += str(current_number) + ' '
        current_number += 1

        if y == x-1:
            print(row_result)
            break
