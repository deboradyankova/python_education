number_of_eggs_player_1 = int(input())
number_of_eggs_player_2 = int(input())

while True:
    command = input()

    if command == 'End of battle':
        print(f'Player one has {number_of_eggs_player_1} eggs left.')
        print(f'Player two has {number_of_eggs_player_2} eggs left.')
        break

    if command == 'one':
        number_of_eggs_player_2 -= 1
    if command == 'two':
        number_of_eggs_player_1 -= 1

    if number_of_eggs_player_1 == 0:
        print(f'Player one is out of eggs. Player two has {number_of_eggs_player_2} eggs left.')
        break
    elif number_of_eggs_player_2 == 0:
        print(f'Player two is out of eggs. Player one has {number_of_eggs_player_1} eggs left.')
        break

