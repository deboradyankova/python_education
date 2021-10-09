whiskey_price = float(input('whiskey price'))
beer_amount = float(input('beer amount'))
wine_amount = float(input('wine amount'))
rakia_amount = float(input('rakia amount'))
whiskey_amount = float(input('whiskey amount'))

rakia_price = whiskey_price / 2
wine_price = rakia_price * 0.6
beer_price = rakia_price * 0.2

total = beer_price * beer_amount \
        + wine_price * wine_amoun \
        + rakia_amount * rakia_price \
        + whiskey_amount * whiskey_price

print(f'{total:.2f}')
