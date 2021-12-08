from sys import maxsize

command = input()

max = -maxsize

while command != 'Stop':

    number = int(command)

    if number > max:
        max = number
        command = input()
    else:
        print(max)
        break
       