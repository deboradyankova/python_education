# first = 100_000
# sec = 100_050
#
# result = ''
#
# for x in range(first, sec+1):
#     enum_current = enumerate(str(x))
#
#     ev_sum = 0
#     odd_sum = 0
#
#     for index, digit in enum_current:
#         if index % 2 == 0:
#             ev_sum += int(digit)
#         else:
#             odd_sum += int(digit)
#
#     if ev_sum == odd_sum:
#         result += f'{x} '
#
# print(result)

name = 'Debora'

enum_name = enumerate(name, start=10)

for index, letter in enum_name:
    print(f'{index} - Index, {letter} - letter')

