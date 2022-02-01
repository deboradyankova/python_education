number_of_chars = int(input())
add = 0

for _ in range(number_of_chars):
    line = input()
    add += ord(line)
print(add)
