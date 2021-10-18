from math import pi

SQUARE = 'square'
RECTANGLE = 'rectangle'
CIRCLE = 'circle'
TRIANGLE = 'triangle'

figure = input('figure type')

area = None
if figure == SQUARE:
    side_a = float(input('length'))
    area = side_a**2
elif figure == RECTANGLE:
    side_a = float(input('length'))
    side_b = float(input('height'))
    area = side_a*side_b
elif figure == CIRCLE:
    r = float(input('radius'))
    area = pi * r**2
else:
    side_a = float(input('length'))
    h = float(input('height'))
    area = side_a*h/2

print(f'{area:.3f}')