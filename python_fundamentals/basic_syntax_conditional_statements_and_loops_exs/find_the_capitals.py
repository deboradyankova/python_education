string = input()

result = []

for index in range(len(string)):
    if string[index].isupper():
        result.append(index)
print(result)

