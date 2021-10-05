CONVERTER_TO_LITERS = 1000
CONVERTER_TO_COEF_FOR_MULTIPLICATION = 100

length = int(input('length in cm:'))
width = int(input('width in cm:'))
height = int(input('height in cm:'))
used_vol_of_items = float(input('used vol of items %')) / CONVERTER_TO_COEF_FOR_MULTIPLICATION

volume = length * width * height
volume_in_liters = volume / CONVERTER_TO_LITERS
items_vol_in_liters = volume_in_liters * used_vol_of_items

needed_water = volume_in_liters - items_vol_in_liters

print(f'{needed_water:.3f}')



