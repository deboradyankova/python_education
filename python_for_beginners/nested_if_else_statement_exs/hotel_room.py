ROOM_PRICES = {
    'studio': {
        'prices': [50, 75.20, 76],
        'discount': [0.95, 0.7, 0.80],
        'months': []
    },
    'apartment': [65, 68.70, 77],
}

ROOM_DISCOUNTS = {
    'studio': [0.95, 0.7, 0.80],
    'apartment': [0.9],
}


def take_price_and_discount_index(days, month, room):
    if days in range(7, 14):
        pass
    elif days > 14:
        pass


month_of_stay = input('month')
number_of_nights = int(input('number of nights'))



