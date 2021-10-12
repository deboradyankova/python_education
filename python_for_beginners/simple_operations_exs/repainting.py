PROTECTIVE_NYLON_PRICE = 1.50
PAINT_LITER_PRICE = 14.50
PAINT_THINNER_PRICE = 5.00
NYLON_BAGS_PRICE = 0.40

protective_nylon_amount = int(input('Protective nylon'))
paint_liters = int(input('Paint liters'))
paint_thinner_amount = int(input('Paint thinner amount'))
working_hours = int(input('Working hours'))

paint_liters = paint_liters * 1.1
protective_nylon_amount += 2
total_materials_price = PROTECTIVE_NYLON_PRICE * protective_nylon_amount \
                        + PAINT_LITER_PRICE * paint_liters \
                        + PAINT_THINNER_PRICE * paint_thinner_amount \
                        + NYLON_BAGS_PRICE
working_price_per_hour = total_materials_price * 0.3
total = total_materials_price + working_price_per_hour * working_hours
print(total)
