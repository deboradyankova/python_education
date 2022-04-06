winnings = {
    1: [[0, 0], [1, 0], [2, 0]],
    2: [[0, 1], [1, 1], [2, 1]],
    3: [[0, 2], [1, 2], [2, 2]],
    4: [[0, 0], [1, 1], [2, 2]],
    5: [[0, 2], [1, 1], [2, 0]]
}
field = [input().split() for _ in range(3)]

# field = []
# for _ in range(3):
#     field.append(input().split())
# print(field)

winner = 0

player_1_fields = []
player_2_fields = []

for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == '0':
            continue

        if field[i].count('1') == 3:
            winner = 'First'
            break
        elif field[i].count('2') == 3:
            winner = 'Second'
            break

        if field[i][j] == '1':
            player_1_fields.append([i, j])
        else:
            player_2_fields.append([i, j])


if player_1_fields in winnings.values():
    winner = 'First'
elif player_2_fields in winnings.values():
    winner = 'Second'

if winner:
    print(f'{winner} player won')
else:
    print('Draw!')