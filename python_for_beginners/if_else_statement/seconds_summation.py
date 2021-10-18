MINUTE = 60

competitor_one = int(input('Competitor one'))
competitor_two = int(input('Competitor two'))
competitor_three = int(input('Competitor three'))

total_seconds = competitor_one \
                + competitor_two \
                + competitor_three

minutes = total_seconds // MINUTE
seconds = total_seconds % MINUTE

if seconds < 10:
   seconds = f'0{seconds}'

print(f'{minutes}:{seconds}')