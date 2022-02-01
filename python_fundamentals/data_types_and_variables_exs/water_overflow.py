CAPACITY_LITERS = 255

n_lines = int(input())

liters = 0

for _ in range(n_lines):
    liters_to_fill = int(input())

    liters += liters_to_fill

    if liters > CAPACITY_LITERS:
        print('Insufficient capacity!')
        liters -= liters_to_fill

print(liters)
