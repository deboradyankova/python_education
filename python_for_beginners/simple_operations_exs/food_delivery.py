CHICKEN_MENU_PRICE = 10.35
FISH_MENU_PRICE = 12.40
VEGETARIAN_MENU_PRICE = 8.15
DELIVERY_PRICE = 2.50

chicken_menu = int(input('Chicken menu'))
fish_menu = int(input('Fish menu'))
vegetarian_menu = int(input('Vegetarian menu'))

menu_cost = CHICKEN_MENU_PRICE * chicken_menu \
            + FISH_MENU_PRICE * fish_menu \
            + VEGETARIAN_MENU_PRICE * vegetarian_menu
desert = menu_cost * 0.2

total = menu_cost + desert + DELIVERY_PRICE

print(total)
