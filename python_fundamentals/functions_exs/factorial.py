def get_factorial(number):
    n = 1

    for x in range(number, 0, -1):
        n *= x
    return n

def get_division_of_two_factorials(n1, n2):
    return f'{n1/n2:.2f}'


n1 = int(input())
n2 = int(input())

n1_factorial = get_factorial(n1)
n2_factorial = get_factorial(n2)

print(get_division_of_two_factorials(n1_factorial, n2_factorial))
