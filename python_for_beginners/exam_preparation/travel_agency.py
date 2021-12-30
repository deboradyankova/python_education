city_price = {
    'banskoborovets': {
        'withequipment': 100,
        'noequipment': 80,
    },
    'varnaburgas': {
        'withbreakfast': 130,
        'nobreakfast': 100,
    },
}

vip_discount_percentage = {
    'bansko': {
        'yes': 0.90,
        'no': 1,
    },
    'borovets': {
        'yes': 0.95,
        'no': 1,
    },
    'varna': {
        'yes': 0.88,
        'no': 1,
    },
    'burgas': {
        'yes': 0.93,
        'no': 1,
    },
}

type_of_city = input().lower()
type_of_package = input().lower()
vip_discount = input().lower()
days = int(input())

key = [k for k in city_price.keys() if type_of_city in k][0]


total_price = days * city_price[key][type_of_package] * vip_discount_percentage[type_of_city][vip_discount]

if days < 1:
    print(f'Days must be positive number!')
elif days >= 1:
    print(f'The price is {total_price:.2f}lv! Have a nice time!')
else:
    print(f'Invalid input!')
