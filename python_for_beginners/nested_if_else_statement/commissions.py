def take_sales_index(prodajbi):
    if 0 <= prodajbi <= 500:
        return 0
    elif 500 < prodajbi <= 1_000:
        return 1
    elif 1_000 < prodajbi <= 10_000:
        return 2
    elif prodajbi > 10_000:
        return 3


COMMISSIONS_PERCENTAGE = {
    'SOFIA': [0.05, 0.07, 0.08, 0.12],
    'VARNA': [0.045, 0.075, 0.10, 0.13],
    'PLOVDIV': [0.055, 0.08, 0.12, 0.145]

}

city = input('City').upper()
sales = float(input('Sales'))

if city in COMMISSIONS_PERCENTAGE.keys() and sales >= 0:
    i = take_sales_index(sales)
    result = COMMISSIONS_PERCENTAGE[city][i] * sales
    print(f'{result:.2f}')
else:
    print('error')
