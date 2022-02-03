n_snowballs = int(input())

max_snowball_snow = None
max_snowball_time = None
max_snowball_quality = None

max_snowball_value = -1

for snowballs in range(n_snowballs):
    snowball_snow = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = int((snowball_snow / snowball_time)) ** snowball_quality

    if snowball_value > max_snowball_value:
        max_snowball_value = snowball_value
        max_snowball_snow = snowball_snow
        max_snowball_time = snowball_time
        max_snowball_quality = snowball_quality

print(f'{max_snowball_snow} : {max_snowball_time} = {max_snowball_value} ({max_snowball_quality})')
