CAKE = 45 * (1 - 0.125)
GOFRETTA = 5.80 * (1 - 0.125)
PANCAKE = 3.20 * (1 - 0.125)

campaign_days = int(input('Campaign days:'))
number_of_bakers = int(input('Number of bakers'))
number_of_cakes = int(input('Number of cakes'))
number_of_gofrettas = int(input('Number of gofrettas'))
number_of_pancakes = int(input('Number of pancakes'))

baker_profit_day = CAKE * number_of_cakes + GOFRETTA * number_of_gofrettas + PANCAKE * number_of_pancakes
team_profit_per_day = baker_profit_day * number_of_bakers
campaign_profit = team_profit_per_day * campaign_days

print(f'{campaign_profit:.2f}')
