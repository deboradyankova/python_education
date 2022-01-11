needed_profit = float(input())

profit = 0

while True:

    name_cocktail = input()

    if name_cocktail == 'Party!':
        print(f'We need {(needed_profit - profit):.1f} leva more.')
        print(f'Club income - {profit:.0f} leva.')
        break

    number_of_cocktails = int(input())

    price_of_cocktail = len(name_cocktail)
    bill_amount = price_of_cocktail * number_of_cocktails

    profit += bill_amount

    if bill_amount % 2 == 1:
        bill_amount = bill_amount * 0.75
        profit = bill_amount

    if needed_profit <= profit:
        print('Target acquired.')
        print(f'Club income - {profit} leva.')
        break
