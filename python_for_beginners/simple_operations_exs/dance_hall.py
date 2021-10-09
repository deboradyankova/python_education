DANCER_AREA = 40 / 10000
DANCER_SPACE_AREA = 7000 / 10000
FULL_AREA_PER_DANCER = DANCER_SPACE_AREA + DANCER_AREA

l_of_hall = float(input('length hall'))
w_of_hall = float(input('width hall'))
a_of_wardrobe = float(input('side wardrobe'))

hall_area = l_of_hall * w_of_hall
wardrobe_area = a_of_wardrobe ** 2
bench_area = hall_area / 10

free_area = hall_area - wardrobe_area - bench_area
capacity = free_area // FULL_AREA_PER_DANCER

print(int(capacity))
