SQUARE_METER_PRICE = 7.61
DISCOUNT = 0.18
FINAL_DISCOUNTED_PRICE = SQUARE_METER_PRICE * (1- DISCOUNT)

square_meters = float(input("square meters "))

final_price = square_meters * FINAL_DISCOUNTED_PRICE
discount = square_meters * SQUARE_METER_PRICE - final_price

print(f"The final price is: {final_price:.2f} lv.")
print(f'The discount is: {discount:.2f} lv.')
