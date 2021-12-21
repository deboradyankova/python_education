floor_number = int(input())
room_number = int(input())

for floor in range(floor_number, 0, -1):

    if floor == floor_number:
        result = [f'L{floor}{room}' for room in range(room_number)]
        print(' '.join(result))
        continue

    if floor % 2 == 0:
        result = [f'O{floor}{room}' for room in range(room_number)]

    else:
        result = [f'A{floor}{room}' for room in range(room_number)]

    print(' '.join(result))
