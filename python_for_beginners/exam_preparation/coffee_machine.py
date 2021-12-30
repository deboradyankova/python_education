WITHOUT_SUGAR_DISCOUNT_PERCENTAGE = 0.65
ESPRESSO_MORE_THAN_5_DISCOUNT_PERCENTAGE = 0.75
TOTAL_PAYMENT_MORE_THAN_15_LEV_DISCOUNT_PERCENTAGE = 0.80

coffee_type_price = {
    'espresso': {
        'without': 0.90,
        'normal': 1,
        'extra': 1.20
    },
    'cappuccino': {
        'without': 1,
        'normal': 1.20,
        'extra': 1.60
    },
    'tea': {
        'without': 0.50,
        'normal': 0.60,
        'extra': 0.70
    }
}

type_of_drink = input().lower()
sugar = input().lower()
number_of_drinks = int(input())

total_payment = coffee_type_price[type_of_drink][sugar] * number_of_drinks

if sugar == 'without':
    total_payment = total_payment * WITHOUT_SUGAR_DISCOUNT_PERCENTAGE
if type_of_drink == 'espresso' and number_of_drinks >= 5:
    total_payment = total_payment * ESPRESSO_MORE_THAN_5_DISCOUNT_PERCENTAGE
if total_payment >= 15:
    total_payment = total_payment * TOTAL_PAYMENT_MORE_THAN_15_LEV_DISCOUNT_PERCENTAGE

print(f'You bought {number_of_drinks} cups of {type_of_drink.capitalize()} for {total_payment:.2f} lv.')
