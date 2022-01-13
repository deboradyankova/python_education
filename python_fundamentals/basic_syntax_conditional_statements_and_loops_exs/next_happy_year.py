def is_happy_year(year):
    for dig in year:
        if year.count(dig) > 1:
            return False
    return True


year = int(input())

while True:
    year += 1

    if is_happy_year(str(year)):
        print(year)
        break
