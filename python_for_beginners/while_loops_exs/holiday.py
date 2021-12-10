money_needed = float(input())
money_on_hand = float(input())

account = 0
days_spending_money = 0
total_days = 0

while True:

    if days_spending_money == 5:
        break

    if money_needed <= money_on_hand:
        break

    action = input()
    current_money = float(input())

    if action == 'spend':
        money_on_hand -= current_money
        if money_on_hand < 0:
            money_on_hand = 0
        days_spending_money += 1
    else:
        money_on_hand += current_money
        days_spending_money = 0
    total_days += 1

if days_spending_money >= 5:
    print('You cant save the money')
    print(days_spending_money)
else:
    print(f'You saved the money {total_days} days')
