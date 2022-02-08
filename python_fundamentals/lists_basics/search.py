number = int(input())
word = input()

lst = []

for _ in range(number):
    strings = input()
    lst.append(strings)

    matches = [match for match in lst if word in match]
print(lst)
print(matches)
