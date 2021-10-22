def my_function(name, age, city):
    name = name.upper()
    age += 5
    city = f'{city} city'
    if age == 3:
        return f'Hello {name}! You are {age} yo from {city}'

    return 'Pedal'


print(my_function('Debora', 23, 'Sofia'))
