def take_discount_index(days):
    if days in range(10):
        return 1
    elif days in range(10, 16):
        return 2
    elif days > 15:
        return 3


ROOM_PRICE_AND_DISCOUNT = {
    'room for one person': [18, 1, 1, 1],
    'apartment': [25, 0.70, 0.65, 0.50],
    'president apartment': [35, 0.90, 0.75, 0.80],
}

POSITIVE_FEEDBACK_PERCENTAGE = 1.25
NEGATIVE_FEEDBACK_PERCENTAGE = 0.90
PRICE_INDEX = 0

days = int(input('days')) - 1
type_room = input('type room').lower()
feedback = input('feedback').lower()

discount_index = take_discount_index(days)
price = ROOM_PRICE_AND_DISCOUNT[type_room][PRICE_INDEX]
final_price = price * ROOM_PRICE_AND_DISCOUNT[type_room][discount_index] * days

if feedback == 'positive':
    final_price = final_price * POSITIVE_FEEDBACK_PERCENTAGE
elif feedback == 'negative':
    final_price = final_price * NEGATIVE_FEEDBACK_PERCENTAGE

print(f'{final_price:.2f}')
