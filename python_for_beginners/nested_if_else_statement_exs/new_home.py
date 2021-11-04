from sys import maxsize

FLOWERS_PRICES = {
    'roses': {
        'price': 5.00,
        'amount_range_for_price_change': range(80, maxsize),
        'coef_for_price_change': 0.9
    },
    'dahlias': {
        'price': 3.80,
        'amount_range_for_price_change': range(90, maxsize),
        'coef_for_price_change': 0.85,
    },
    'tulips': {
        'price': 2.80,
        'amount_range_for_price_change': range(80, maxsize),
        'coef_for_price_change': 0.85,
    },
    'narcissus': {
        'price': 3.00,
        'amount_range_for_price_change': range(0, 120),
        'coef_for_price_change': 1.15,
    },
    'gladiolus': {
        'price': 2.50,
        'amount_range_for_price_change': range(0, 80),
        'coef_for_price_change': 1.20,
    },
}

flower_type = input('Flower type: ').lower()
flowers_amount = int(input('Flowers amount: '))
budget = int(input('Budget: '))

total = FLOWERS_PRICES[flower_type]['price'] * flowers_amount
if flowers_amount in FLOWERS_PRICES[flower_type]['amount_range_for_price_change']:
    total = total * FLOWERS_PRICES[flower_type]['coef_for_price_change']

diff = abs(total - budget)
if budget >= total:
    print(f'Hey, you have a great garden with {flowers_amount} {flower_type} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
