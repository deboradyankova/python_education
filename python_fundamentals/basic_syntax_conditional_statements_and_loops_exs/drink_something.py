def get_type_of_drink(age):
    if age in range(14):
        return 'toddy'
    elif age in range(14, 18):
        return 'coke'
    elif age in range(18, 21):
        return 'beer'
    return 'whisky'


years = int(input())

drink = get_type_of_drink(years)
print(f'drink {drink}')
