loop = int(input('loop'))

division_2 = 0
division_3 = 0
division_4 = 0

for _ in range(loop):
    number = int(input())

    if number % 2 == 0:
        division_2 += 1
    if number % 3 == 0:
        division_3 += 1
    if number % 4 == 0:
        division_4 += 1

p1 = division_2 / loop * 100
p2 = division_3 / loop * 100
p3 = division_4 / loop * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
