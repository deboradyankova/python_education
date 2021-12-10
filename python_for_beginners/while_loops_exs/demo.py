money_enough = False

money_need = 100

while not money_enough:

    money_get = int(input())

    if money_get > money_need:
        money_enough = True
