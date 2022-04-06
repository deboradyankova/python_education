def calculation(command, b, c):
    calculations = {
        'multiply': b * c,
        'divide': b / c,
        'add': b + c,
        'subtract': b - c,
    }
    return calculations[command]


operator = input()
parameter_one = int(input())
parameter_two = int(input())

print(calculation(operator, parameter_one, parameter_two))
