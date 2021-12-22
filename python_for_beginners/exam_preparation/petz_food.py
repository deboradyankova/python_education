import datetime

days = int(input())
food_amount = float(input())

dogs = 0
cats = 0
biscuits = 0

start = datetime.datetime.now()

for day in range(1, days + 1):
    dogs_food = int(input())
    cats_food = int(input())

    dogs += dogs_food
    cats += cats_food

    if day % 3 == 0:
        biscuits += (dogs_food + cats_food) * 0.1

total = dogs + cats
total_eaten_pct = total / food_amount * 100
dogs_pct = dogs / total * 100
cats_pct = cats / total * 100

print(f'Total eaten biscuits: {biscuits:.0f}gr.')
print(f'{total_eaten_pct:.2f}% of the food has been eaten.')
print(f'{dogs_pct:.2f}% eaten from the dog.')
print(f'{cats_pct:.2f}% eaten from the cat.')

end = datetime.datetime.now()

print(end - start)
