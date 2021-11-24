letters_value = {
    'a': 1,
    'e': 2,
    'i': 3,
    'o': 4,
    'u': 5,
}

result = 0
string = input('string')

for letter in string:
    if letter in letters_value.keys():
        result += letters_value[letter]
print(result)
