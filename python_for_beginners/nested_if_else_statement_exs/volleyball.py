import math

WEEKENDS_FULL_YEAR = 48
PLAYS_IN_SOFIA_HOLIDAYS = 2 / 3
DAYS_OFF_IN_SOFIA = 3 / 4
PLAYS_LEAP_YEAR_PERCENTAGE = 1.15

year = input('year')
p = int(input('holidays'))
h = int(input('weekends'))

stay_in_sofia = 48 - h
plays_in_sofia_holiday = stay_in_sofia * DAYS_OFF_IN_SOFIA
plays_in_sofia_weekends = p * PLAYS_IN_SOFIA_HOLIDAYS

if year == 'normal':
    plays_full_year = plays_in_sofia_holiday + plays_in_sofia_weekends + h
    print(math.floor(plays_full_year))
elif year == 'leap':
    plays_full_year = (plays_in_sofia_holiday + plays_in_sofia_weekends + h) * PLAYS_LEAP_YEAR_PERCENTAGE
    print(math.floor(plays_full_year))
