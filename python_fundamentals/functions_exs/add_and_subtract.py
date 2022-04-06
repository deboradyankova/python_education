def sum_numbers(num_one, num_two):
    return num_one + num_two


def subtract(num_one, num_two):
    return num_one - num_two


def add_and_subtract(n1, n2, n3):
    summed = sum_numbers(n1, n2)
    subtracted = subtract(summed, n3)
    return subtracted


num_one = int(input())
num_two = int(input())
num_three = int(input())

res = add_and_subtract(num_one, num_two, num_three)
print(res)

