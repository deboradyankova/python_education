FRUIT_PRICES = {
    'banana': [2.5, 2.70],
    'apple': [1.20, 1.25],
    'orange': [0.85, 0.90],
    'grapefruit': [1.45, 1.60],
    'kiwi': [2.70, 3.00],
    'pineapple': [5.50, 5.60],
    'grapes': [3.85, 4.20],
}

WEEK_INDEX = 0
WEEKEND_INDEX = 1

WEEKDAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', ]

fruit = input('fruit')
day = input('day')
amount = float(input('amount'))

result = FRUIT_PRICES[fruit]

if day in WEEKDAYS:
    result = result[WEEK_INDEX] * amount
else:
    result = result[WEEKEND_INDEX]*amount

print(result)


