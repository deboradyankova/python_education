flock = input().split(', ')

for sheep_number in range(len(flock)):
    animal = flock.pop()

    if animal == 'wolf':
        if sheep_number == 0:
            print('Please go away and stop eating my sheep')
        else:
            print(f'Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!')
        break
