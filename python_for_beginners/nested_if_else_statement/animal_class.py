# example one

animal = input('Animal')

if animal == 'dog':
    print('mammal')
elif animal == 'crocodile' \
        or animal == 'snake' \
        or animal == 'tortoise':
    print('reptile')
else:
    print('unknown')

# example two
animal = input('animal')
animal_class = ''

if animal == 'dog':
    animal_class = 'mammal'
elif animal == 'crocodile':
    animal_class = 'reptile'
elif animal == 'snake':
    animal_class = 'reptile'
elif animal == 'tortoise':
    animal_class = 'reptile'
else:
    animal_class = 'unknown'

print(animal_class)

# example three

animal = input('animal')
animal_class = ''

if animal == 'dog':
    animal_class = 'mammal'
elif animal == 'crocodile' \
        or animal == 'snake' \
        or animal == 'tortoise':
    animal_class = 'reptile'
else:
    animal_class = 'unknown'

print(animal_class)

# example four

mammals = ['dog']
reptiles = ['snake', 'tortoise', 'crocodile']

animal = input()

if animal in mammals:
    print('mammal')
elif animal in reptiles:
    print('reptile')
else:
    print('unknown')

