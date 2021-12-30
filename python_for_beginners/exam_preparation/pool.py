import math

number_of_people = int(input())
entrance_fee = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

entrance_fee_per_person = number_of_people * entrance_fee
sunbed_per_person = math.ceil(0.75 * number_of_people)
umbrella_per_person = math.ceil(number_of_people / 2)

total_sunbed_price = sunbed_per_person * sunbed_price
total_umbrella_price = umbrella_price * umbrella_per_person

total_fee = total_umbrella_price + total_sunbed_price + entrance_fee_per_person

print(f'{total_fee:.2f} lv.')
