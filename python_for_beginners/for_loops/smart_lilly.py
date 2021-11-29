lillys_age = int(input('age'))
price_washing_machine = float(input('price washing machine'))
price_per_toy = int(input('price per toy'))

toys_count = lillys_age // 2
if lillys_age % 2 == 1:
    toys_count += 1
savings = toys_count * price_per_toy
present_amount = 10

for year in range(2, lillys_age + 1, 2):
    savings += present_amount - 1
    present_amount += 10

if savings >= price_washing_machine:
    print(f'Yes! {savings - price_washing_machine}')
else:
    print(f'No! {price_washing_machine - savings}')




