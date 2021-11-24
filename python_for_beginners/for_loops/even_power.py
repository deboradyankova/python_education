# number = int(input('number'))
#
# for number in range(0, number + 1):
#     if number % 2 == 0:
#         print(2 ** number)

number = int(input('number'))

for number in range(0, number + 1, 2):
    print(2 ** number)
