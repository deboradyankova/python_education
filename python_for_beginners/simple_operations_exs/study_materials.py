PEN_PACK = 5.80
MARKERS_PACK = 7.20
DETERGENT_LITER = 1.20

number_pen_pack = int(input('number pen pack'))
number_markers_pack = int(input('number markers pack'))
detergent_liters = int(input('detergent liters'))
discount = int(input('discount'))

total_pen_pack = PEN_PACK * number_pen_pack
total_markets_pack = MARKERS_PACK * number_markers_pack
total_detergent_liters = DETERGENT_LITER * detergent_liters
total_materials = total_pen_pack + total_markets_pack + total_detergent_liters
total_money = total_materials * (1 - discount / 100)

print(total_money)
