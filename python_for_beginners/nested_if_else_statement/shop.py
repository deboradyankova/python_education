# product_price_sofia = {
#     'coffee': 0.5,
#     'water': 0.8,
#     'beer': 1.20,
#     'sweets': 1.45,
#     'peanuts': 1.60,
# }
# product_price_plovdiv = {
#     'coffee': 0.40,
#     'water': 0.70,
#     'beer': 1.15,
#     'sweets': 1.30,
#     'peanuts': 1.50,
# }
# product_price_varna = {
#     'coffee': 0.45,
#     'water': 0.7,
#     'beer': 1.10,
#     'sweets': 1.35,
#     'peanuts': 1.55,
# }
#
# product = input('product')
# city = input('city')
# amount = float(input('amount'))
#
# if product in product_price_sofia.keys():
#
#     print(f'Price is {amount * product_price_sofia[product]:.2f}')
#
# elif product in product_price_plovdiv.keys():
#     print(f'Price is {amount * product_price_plovdiv[product]:.2f}')
# elif product in product_price_varna.keys():
#     print(f'Price is {amount * product_price_varna[product]:.2f}')

indices = {
    'SOFIA': 0,
    'PLOVDIV': 1,
    'VARNA': 2,
    'BURGAS': 3,
}
product_prices = {
    'coffee': [
        0.5,
        0.4,
        0.45,
        0.42,
    ],
    'water': [
        0.8,
        0.7,
        0.7,
        0.75,
    ],
    'beer': [
        1.2,
        1.15,
        1.1,
        1,
    ],
    'sweets': [
        1.45,
        1.3,
        1.35,
        1.20,
    ],
    'peanuts': [
        1.6,
        1.5,
        1.55,
        1.25,
    ],
}


product = input('product')
city = input('city').upper()
amount = float(input('amount'))

if product in product_prices.keys() and city in indices.keys():
    result = product_prices[product][indices[city]] * amount
    print(f'{result:.2f}')
