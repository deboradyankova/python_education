number = int(input('number'))
result = ''

# if number != 0:
#     if number >= -100 and number <= 100:
#         print('yes')
# else:
#     print('no')

if number in range(-100, 101) and number != 0:
    result = "yes"
else:
    result = "no"
print(result)
