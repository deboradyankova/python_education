from sys import maxsize

command = input()

minimum = maxsize

while command != 'Stop':

    number = int(command)

    if number < minimum:
        minimum = number
        command = input()
else:
    print(minimum)


    

