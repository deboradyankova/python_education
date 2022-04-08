def get_sum_of_divisors(number):
    sum_of_divisors = 0
    for n in range(1, number // 2 + 1):
        if number % n == 0:
            sum_of_divisors += n
    return sum_of_divisors


def is_perfect_number(number, divisors_sum):
    if number == divisors_sum:
        return True
    return False


n = int(input())

sum_of_divisors = get_sum_of_divisors(n)
is_perfect = is_perfect_number(n, sum_of_divisors)

if is_perfect:
    print('We have a perfect number!')
else:
    print('It\'s not so perfect.')
