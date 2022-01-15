decoration_prices = {
    'ornament set': 2,
    'tree skirt': 5,
    'tree garlands': 3,
    'tree lights': 15,
}

quantity = int(input())
days = int(input())

total_spirit = 0
total_cost = 0

for day in range(2, days+1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_spirit += 5
        total_cost += decoration_prices['ornament set'] * quantity
    if day % 3 == 0:
        total_spirit += 13
        total_cost += (
            decoration_prices['tree skirt'] +
            decoration_prices['tree garlands']
        ) * quantity
    if day % 5 == 0:
        total_spirit += 17
        total_cost += decoration_prices['tree lights'] * quantity
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += (
            decoration_prices['tree skirt'] +
            decoration_prices['tree garlands'] +
            decoration_prices['tree lights']
        )
        if day == days:
            total_spirit -= 30


print(f'cost {total_cost}')
print(f'spirit {total_spirit}')

