TABLE_CLOTH_DELTA = 0.6
TABLE_CLOTH_TEXTILE_PRICE = 7
CARRE_TEXTILE_PRICE = 9
USD_TO_BGN = 1.85

number_of_tables = int(input('Rectangular tables'))
table_length = float(input('Tables length'))
table_width = float(input('Table width'))

area_table_cloth = (table_length + TABLE_CLOTH_DELTA) * (table_width + TABLE_CLOTH_DELTA)
carre_side = table_length / 2
area_carre = carre_side ** 2

needed_table_cloth = number_of_tables * area_table_cloth
needed_carre_cloth = number_of_tables * area_carre

cloth_price = needed_table_cloth * TABLE_CLOTH_TEXTILE_PRICE
carre_price = needed_carre_cloth * CARRE_TEXTILE_PRICE

total_usd = carre_price + cloth_price
total_bgn = total_usd * USD_TO_BGN

print(f'{total_usd:.2f} USD')
print(f'{total_bgn:.2f} BGN')
