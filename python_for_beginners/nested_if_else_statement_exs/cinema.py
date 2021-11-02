TICKET_PRICE = {
    'PREMIERE': 12,
    'NORMAL': 7.5,
    'DISCOUNT': 5,
}

type_projection = input('type projection').upper()
number_columns = int(input('columns'))
number_rows = int(input('rows'))

cinema_hall = number_rows * number_columns
full_cinema_hall_income = cinema_hall * TICKET_PRICE[type_projection]

if type_projection in TICKET_PRICE.keys():
    result = full_cinema_hall_income
    print(f'{result:.2f} leva')
