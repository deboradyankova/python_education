factor = input()
count = input()

lst = []

for counter in range(1, int(count) + 1):
    lst.append(counter)

new_lst = [x * int(factor) for x in lst]

print(new_lst)

