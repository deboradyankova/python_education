def get_ASCII_range(first_char, second_char):
    result = ''
    for ascii_num in range(ord(first_char) + 1, ord(second_char)):
        result += f'{chr(ascii_num)} '
    return result


char_one = input()
char_two = input()

print(get_ASCII_range(char_one, char_two))
