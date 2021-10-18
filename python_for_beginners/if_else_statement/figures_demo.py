from math import pi


def area_square():
    side_a = float(input('length'))
    return side_a ** 2


def area_rectangle():
    side_a = float(input('length'))
    side_b = float(input('height'))
    return side_a * side_b


def area_circle():
    r = float(input('radius'))
    return pi * r ** 2


def area_triangle():
    side_a = float(input('length'))
    h = float(input('height'))
    return side_a * h / 2


types = {
    'SQUARE': area_square,
    'RECTANGLE': area_rectangle,
    'CIRCLE': area_circle,
    'TRIANGLE': area_triangle,
}

figure = input('figure type').upper()

try:
    area = types[figure]
    area = area()
    print(f'{area:.3f}')
except KeyError:
    print('Wrong input')