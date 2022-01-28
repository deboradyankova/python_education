number_coffee = 0

while True:
    command = input()

    if command == 'END':
        break
    if command == 'dog':
        number_coffee -= 1

    command = [command]
    for i in range(len(command)):

        if command[i] == command[i].lower():
            number_coffee += 1
        elif command[i] == command[i].upper():
            number_coffee += 2

if number_coffee > 5:
    print('You need extra sleep')
else:
    print(number_coffee)
