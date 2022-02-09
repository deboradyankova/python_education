team_a_players = 11
team_b_players = 11

cards_list = set(input().split())

is_terminated = False

for player in cards_list:
    if player.startswith('A'):
        team_a_players -= 1
    else:
        team_b_players -= 1

    if team_a_players < 7 or team_b_players < 7:
        is_terminated = True
        break

print(f'Team A - {team_a_players}; Team B - {team_b_players}')
if is_terminated:
    print('Game was terminated')