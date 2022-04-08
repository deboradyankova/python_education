def palindrome_flag(n):
    if n == n[::-1]:
        return True
    return False

line = input().split(', ')

for n in line:
    print(palindrome_flag(n))

