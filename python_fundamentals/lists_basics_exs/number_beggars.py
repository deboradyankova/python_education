numbers = [int(n) for n in input().split(', ')]
number_beggars = int(input())


result = []

for beggar in range(number_beggars):
    beggar_result = 0
    for index in range(beggar, len(numbers), number_beggars):
        if index < len(numbers):
            beggar_result += numbers[index]
    result.append(beggar_result)

print(result)
