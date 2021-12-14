money_available = 0

while True:
    destination = input()

    if destination == 'End':
        break

    needed_budget = float(input())

    while True:
        saved_money = float(input())
        needed_budget -= saved_money
        if needed_budget <= 0:
            print(f'Going to {destination}!')
            break
