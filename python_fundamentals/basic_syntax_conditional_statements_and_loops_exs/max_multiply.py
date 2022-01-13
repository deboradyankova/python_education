divider = int(input())
bound = int(input())

for n in range(bound, 0, -1):
    if n % divider == 0:
        print(n)
        break
