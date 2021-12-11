length = int(input())
width = int(input())

cake_pieces = length * width


while True:

    command = input()
    if command == 'STOP':
        break

    taken_pieces = int(command)

    cake_pieces -= taken_pieces
    if cake_pieces <= 0:
        break

if cake_pieces >= 0:
    print(f'{cake_pieces} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_pieces)} pieces more.')


