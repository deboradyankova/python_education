PRICE_DISCOUNT_NIGHT = 0.05

budget = float(input('budget'))
number_of_nights = int(input('nights'))
price_night = float(input('price per night'))
percentage_additional_expenses = int(input('additional expenses percentage'))

budget_after_additional_expenses = budget - percentage_additional_expenses / 100 * budget

total_cost_per_nights = number_of_nights * price_night
cost_after_price_discount_night = total_cost_per_nights - PRICE_DISCOUNT_NIGHT * total_cost_per_nights

if number_of_nights > 7:
    if budget_after_additional_expenses > cost_after_price_discount_night:
        print(f'Ivanovi will be left with {budget_after_additional_expenses - cost_after_price_discount_night} leva after vacation')

    else:
        print(f'{cost_after_price_discount_night - budget_after_additional_expenses:.2f} leva needed.')

elif number_of_nights > 0 and number_of_nights <= 7:
    if budget_after_additional_expenses > total_cost_per_nights:

        print(f'Ivanovi will be left with {budget_after_additional_expenses - total_cost_per_nights:.2f} leva after vacation')
    else:
        print(f'{abs(total_cost_per_nights - budget_after_additional_expenses)} leva needed')
