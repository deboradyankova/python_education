PUZZLE_PRICE = 2.60
TALKING_DOLL_PRICE = 3.00
TEDDY_BEAR_PRICE = 4.10
MINION_PRICE = 8.20
TRUCK_PRICE = 2.00

excursion_price = float(input('Excursion price'))
puzzle_count = int(input('Puzzle count'))
talking_doll_count = int(input('Talking doll count'))
teddy_bear_count = int(input('Teddy bear count'))
minion_count = int(input('Minion count'))
truck_count = int(input('Truck count'))

total_toys_count = puzzle_count \
                   + talking_doll_count \
                   + teddy_bear_count \
                   + minion_count \
                   + truck_count
total_toys_price = puzzle_count * PUZZLE_PRICE \
                   + talking_doll_count * TALKING_DOLL_PRICE \
                   + teddy_bear_count * TEDDY_BEAR_PRICE \
                   + minion_count * MINION_PRICE \
                   + truck_count * TRUCK_PRICE

if total_toys_count >= 50:
    total_toys_price = total_toys_price * 0.75
total_toys_price = total_toys_price * 0.90

if excursion_price > total_toys_price:
    print(f'Not enough money! {(excursion_price - total_toys_price):.2f} lv needed.')
else:
    print(f'Yes! {(total_toys_price - excursion_price):.2f} lv left.')
