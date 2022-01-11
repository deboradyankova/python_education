prices = {
    'BASKET': 1.50,
    'WREATH': 3.80,
    'CHOCOLATE BUNNY': 7,
}

clients = int(input())
total_bill = 0

for client in range(clients):
    client_bill = 0
    goods_amount = 0

    while True:
        purchase = input().upper()

        if purchase == 'FINISH':

            if goods_amount % 2 == 0:
                client_bill = client_bill * 0.80
            total_bill += client_bill
            print(f'You purchased {goods_amount} items for {client_bill:.2f} leva.')
            break

        client_bill += prices[purchase]
        goods_amount += 1

average_bill_per_client = total_bill / clients
print(f'Average bill per client is: {average_bill_per_client:.2f} leva')

