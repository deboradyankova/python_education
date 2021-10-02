DOG_FOOD = 2.5
OTHER_FOOD = 4

dogs_number = int(input('Enter dogs number: '))
other_animals = int(input('Enter other animals number: '))

result = DOG_FOOD * dogs_number + OTHER_FOOD * other_animals
print(f'{result:.2f} lv.')


