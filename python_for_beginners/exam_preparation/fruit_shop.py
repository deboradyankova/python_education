strawberries_price = float(input('strawberries price'))
bananas_kg = float(input('bananas amount'))
oranges_kg = float(input('oranges amount'))
raspberries_kg = float(input('raspberries amount'))
strawberries_kg = float(input('strawberries amount'))

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price - raspberries_price * 0.4
bananas_price = raspberries_price - raspberries_price * 0.8

total_strawberries_price = strawberries_price * strawberries_kg
total_bananas_price = bananas_price * bananas_kg
total_oranges_price = oranges_price * oranges_kg
total_raspberries_price = raspberries_price * raspberries_kg

total_money_needed = total_strawberries_price \
                     + total_bananas_price + \
                     total_oranges_price + \
                     total_raspberries_price

print(f'{total_money_needed:.2f}')
