first_number = int(input())
second_number = int(input())
result = ''

for x in range(first_number, second_number + 1):
    current_number = str(x)
    even_sum = 0
    odd_sum = 0

    for index in range(len(current_number)):
        if index %2 == 0:
            even_sum += int(current_number[index])
        else:
            odd_sum += int(current_number[index])

    if even_sum == odd_sum:
        result += f'{current_number} '

    even_sum = 0
    odd_sum = 0

print(result)

