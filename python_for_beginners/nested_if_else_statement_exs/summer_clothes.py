outfits = ['T-Shirt', 'Shirt', 'Sweatshirt', 'Swim suit', ]
shoes = ['Sneakers', 'Moccasins', 'Sandals', 'Barefoot', ]

combs = [(2, 1), (1, 1), (0, 2), (3, 3)]

mapper = {
    10_18: {
        'morning': combs[0],
        'afternoon': combs[1],
        'evening': combs[1]
    },
    19_24: {
        'morning': combs[1],
        'afternoon': combs[2],
        'evening': combs[1]
    },
    25: {
        'morning': combs[2],
        'afternoon': combs[3],
        'evening': combs[1]
    }
}

degrees = int(input('degrees'))
time_of_the_day = input('time of the day').lower()

if degrees in range(10, 19):
    outfit, shoe = mapper[10_18][time_of_the_day]
elif degrees in range(18, 25):
    outfit, shoe = mapper[19_24][time_of_the_day]
elif degrees >= 25:
    outfit, shoe = mapper[25][time_of_the_day]

outfit = outfits[outfit]
shoe = shoes[shoe]

print(f'It\'s {degrees} degrees, get your {outfit} and {shoe}.')
