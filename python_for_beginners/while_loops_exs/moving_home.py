width = int(input())
length = int(input())
height = int(input())

available_slots = width * length * height


while True:
    command = input()
    if command == 'Done':
        break
    number_of_boxes = int(command)
    available_slots -= number_of_boxes
    if available_slots <= 0:
        break

if available_slots <= 0:
    print(f'No more free space! You need {abs(available_slots)} Cubic meters more.')
else:
    print(f'{available_slots} Cubic meters left.')


