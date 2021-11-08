def discount_index(number_of_people):
    if number_of_people in range(7):
        return 0.9
    elif number_of_people in range(7, 12):
        return 0.85
    elif number_of_people >= 12:
        return 0.75


PRICES_FOR_RENT = {
    'spring': 3000,
    'summer': 4200,
    'autumn': 4200,
    'winter': 2600,

}

budget = int(input('budget'))
season = input('season').lower()
number_of_people = int(input('number of people'))

total_price = discount_index(number_of_people) * PRICES_FOR_RENT[season]

if season != 'autumn' and number_of_people %2 == 0:
    total_price = total_price * 0.95

if budget >= total_price:
    print(f'Yes! You have {budget - total_price:.2f} leva left.')
else:
    print(f'Not enough money! You need {total_price - budget:.2f} leva.')
