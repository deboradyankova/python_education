coins_list = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

sum_change = float(input())

coins = 0
index = 0

while True:
    if sum_change == 0:
        break

    sum_change -= coins_list[index]
    sum_change = round(sum_change, 2)
    if sum_change < 0:
        sum_change += coins_list[index]
        if index == len(coins_list) - 1:
            continue
        index += 1
        continue
    coins += 1

print(coins)
