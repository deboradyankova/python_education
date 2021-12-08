# command = input()
#
# balance = 0
#
# while command != "NoMoreMoney":
#
#     sum_payment = float(command)
#
#     if sum_payment < 0:
#         print('Invalid operation')
#         break
#     else:
#         print(f'Increase: {sum_payment}')
#         balance += sum_payment
#     command = input()
#
# print(f'Total {balance:.2f}')
#
#
#
#
#

sum_to_add = input()

balance = 0

while True:

    if sum_to_add == 'NoMoreMoney':
        break

    balance += float(sum_to_add)
    print(f'Increase with {sum_to_add}')

    sum_to_add = input()

print(balance)
