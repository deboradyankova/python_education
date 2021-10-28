TIME_HOURS = 24
DELTA_MINUTES = 15

hours = int(input('Hours'))
minutes = int(input('Minutes'))

minutes = minutes + DELTA_MINUTES

if minutes == 60:
    minutes = 0
    hours += 1

if minutes > 60:
    minutes = minutes - 60
    hours += 1

if hours == 24:
    hours = 0

if minutes < 10:
    minutes = f'0{minutes}'
print(f'{hours}:{minutes}')
