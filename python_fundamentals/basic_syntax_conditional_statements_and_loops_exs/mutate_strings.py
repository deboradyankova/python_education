first = list(input())
second = list(input())

for index in range(len(first)):
    if first[index] != second[index]:
        first[index] = second[index]
        print(''.join(first))
