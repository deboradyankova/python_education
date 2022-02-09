data = [1, 2, 4, -10, 30, 'asd', 'jfjkd']

lst_positive = []
lst_negative = []

for el in data:
    try:
        int(el)
    except ValueError:
        continue
    if el > 0:
        lst_positive.append(el)
    else:
        lst_negative.append(el)

print('OK')