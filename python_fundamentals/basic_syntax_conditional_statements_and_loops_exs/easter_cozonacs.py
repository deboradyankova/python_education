budget = float(input())
price_1_kg_flour = float(input())

price_eggs = price_1_kg_flour * 0.75
price_1l_milk = price_1_kg_flour * 1.25
price_1_cozonac_milk = price_1l_milk / 4

price_1_cozonac = price_1_kg_flour + price_eggs + price_1_cozonac_milk

number_of_cozonacs = 0
colored_eggs = 0
n = 3

while True:

    if budget < price_1_cozonac:
        break

    budget -= price_1_cozonac
    number_of_cozonacs += 1
    colored_eggs += 3

    if number_of_cozonacs % n == 0:
        colored_eggs -= number_of_cozonacs - 2


print(f'You made {number_of_cozonacs} cozonacs! Now you have {colored_eggs} eggs and {budget:.2f}BGN left')
