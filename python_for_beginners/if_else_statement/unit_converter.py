from itertools import permutations

METER_MM = 1000
METER_CM = 100

number = float (input('Number'))
unit = str(input('Unit'))
unit_input = str(input('Unit input'))
unit_output = str(input('Unit output'))


perm = permutations(['mm', 'cm', 'm'], 2)
for i in list(perm):
    print (i)
