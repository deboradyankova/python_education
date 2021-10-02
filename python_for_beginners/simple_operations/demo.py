text = "Hello"
number_int = 2
number_float = "Peter"
text_string = "Bobi"

print(text)

print(text)
print(text)
print(text)

result = number_int + number_float
print(result)

user_input = input('Insert a number')

try:
    user_input = int(user_input)
    user_input += 5
except ValueError:
    print('Try again')