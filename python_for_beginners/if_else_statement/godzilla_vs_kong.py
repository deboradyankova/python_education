DECOR = 0.10
NUMBER_STATISTS_DISCOUNT = 0.90

budget = float(input('Budget'))
number_statists = int(input('Super'))
price_clothing_per_statist = float(input('Price clothing'))

decor_film_price = budget * DECOR

if number_statists >= 150:
    price_clothing_per_statist = price_clothing_per_statist * NUMBER_STATISTS_DISCOUNT

statists_expenses = number_statists * price_clothing_per_statist
expenses = decor_film_price + statists_expenses

if expenses >= budget:
    print(f'Not enough money Wingard needs {(expenses - budget):.2f} leva more')
else:
    print(f'Action! Wingard startas filming with {(budget - expenses):.2f} leva left')
