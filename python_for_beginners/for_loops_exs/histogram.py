loop = int(input('loop'))

numbers_to_199 = 0
numbers_from_200_to_399 = 0
numbers_from_400_to_599 = 0
numbers_from_600_to_799 = 0
numbers_over_800 = 0

for _ in range(loop):
    number = int(input())

    if number in range(200):
        numbers_to_199 += 1
    elif number in range(200, 400):
        numbers_from_200_to_399 += 1
    elif number in range(400, 600):
        numbers_from_400_to_599 += 1
    elif number in range(600, 800):
        numbers_from_600_to_799 += 1
    elif number >= 800:
        numbers_over_800 += 1

p1 = numbers_to_199 / loop * 100
p2 = numbers_from_200_to_399 / loop * 100
p3 = numbers_from_400_to_599 / loop * 100
p4 = numbers_from_600_to_799 / loop * 100
p5 = numbers_over_800 / loop * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')
