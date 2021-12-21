prime_numbers_sum = 0
composite_numbers_sum = 0

while True:
    number = input()
    if number == 'stop':
        break

    number = int(number)

    if number < 0:
        print("Number is negative.")
        continue

    is_prime = False

    for div in range(2, number):
        if number % div == 0:
            composite_numbers_sum += number
            break
        if div == number - 1:
            is_prime = True
            break

    if is_prime:
        prime_numbers_sum += number

print(f'Sum of all prime numbers is: {prime_numbers_sum}')
print(f'Sum of all non prime numbers is: {composite_numbers_sum}')
