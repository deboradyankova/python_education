keys = ['sand', 'water', 'fish', 'sun']

string = input().lower()

result = 0

for word in keys:
    if word in string:
        count = string.count(word)
        result += count

print(result)
