def get_even_odd_sums(number):
    even_sum = 0
    odd_sum = 0
    for n in number:
        if int(n) % 2 == 0:
            even_sum += int(n)
        else:
            odd_sum += int(n)
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'

single_number = input()

print(get_even_odd_sums(single_number))