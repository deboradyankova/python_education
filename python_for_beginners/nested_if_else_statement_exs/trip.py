from math import ceil


def get_destination_and_hosting_type(budget, season):
    budget = ceil(budget)
    hosting = {
        'summer': 'camp',
        'winter': 'hotel',
    }
    if budget in range(101):
        return 'bulgaria', hosting[season]
    elif budget in range(100, 1001):
        return 'balkans', hosting[season]
    elif budget > 1000:
        return 'europe', 'hotel'


TRIP_DESTINATION_PRICE = {
    'bulgaria': {
        'summer': 0.30,
        'winter': 0.70,
    },
    'balkans': {
        'summer': 0.40,
        'winter': 0.80,
    },
    'europe': 0.90,

}

budget = float(input('budget'))
season = input('season').lower()

destination, hosting_type = get_destination_and_hosting_type(budget, season)

if destination != 'europe':
    total_trip_cost = TRIP_DESTINATION_PRICE[destination][season] * budget
else:
    total_trip_cost = TRIP_DESTINATION_PRICE[destination] * budget

print(f'Somewhere in {destination.capitalize()}')
print(f'{hosting_type.capitalize()} - {total_trip_cost:.2f}')
