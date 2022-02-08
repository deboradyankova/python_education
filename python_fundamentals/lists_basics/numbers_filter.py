numbers = []

lines = int(input())

for _ in range(lines):
    number = int(input())
    numbers.append(number)

command = input()

if command == 'even':
    numbers = [n for n in numbers if n % 2 == 0]
elif command == 'odd':
    numbers = [n for n in numbers if n % 2 != 0]
elif command == 'negative':
    numbers = [n for n in numbers if n < 0]
else:
    numbers = [n for n in numbers if n > 0]


print(numbers)