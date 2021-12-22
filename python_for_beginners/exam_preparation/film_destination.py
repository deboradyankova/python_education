TAX_RELIEF_DUBAI = 0.30
TAX_SOFIA = 0.25
TAX_LONDON = 0

destination_season_price_per_day = {
    'DUBAI': {
        'WINTER': 45000,
        'SUMMER': 40000
    },
    'SOFIA': {
        'WINTER': 17000,
        'SUMMER': 12500
    },
    'LONDON': {
        'WINTER': 24000,
        'SUMMER': 20250
    }
}

budget_movie = float(input())
destination = input().upper()
season = input().upper()
number_of_days = int(input())

total_budget = number_of_days * destination_season_price_per_day[destination][season]

if destination == 'DUBAI':
    budget_dubai = total_budget - TAX_RELIEF_DUBAI * total_budget
    if budget_movie >= budget_dubai:
        print(f'The budget for the movie is enough! We have {budget_movie - budget_dubai:.2f} leva left!')
    else:
        print(f'The director needs {abs(budget_dubai - budget_movie):.2f} leva more!')
if destination == 'SOFIA':
    budget_sofia = total_budget + TAX_SOFIA * total_budget
    if budget_movie >= budget_sofia:
        print(f'The budget for the movie is enough! We have {budget_movie - budget_sofia:.2f} leva left!')
    else:
        print(f'The director needs {abs(budget_sofia - budget_movie):.2f} leva more!')
if destination == 'LONDON':
    budget_london = total_budget + TAX_LONDON * total_budget
    if budget_movie >= budget_london:
        print(f'The budget for the movie is enough! We have {budget_movie - budget_london:.2f} leva left!')
    else:
        print(f'The director needs {abs(budget_london - budget_movie):.2f} leva more!')