def length_validator(password):
    if len(password) in range(6, 11):
        return True
    return False


def letters_and_digits_validator(password):
    for ch in password:
        if not ch.isdigit() and not ch.isalpha():
            return False

    return True

def min_count_of_digits_validator(password):
    digits_count = 0
    for ch in password:
        if ch.isdigit():
            digits_count += 1
        if digits_count >= 2:
            return True
    return False

def password_validation(password):
    length_check = length_validator(password)
    if not length_check:
        print('Password must be between 6 and 10 characters')
    letters_and_digits_check = letters_and_digits_validator(password)
    if not letters_and_digits_check:
        print('Password must consist only of letters and digits')
    min_count_check = min_count_of_digits_validator(password)
    if not min_count_check:
        print('Password must have at least 2 digits')
    if length_check and letters_and_digits_check and min_count_check:
        print('Password is valid')

password = input()

password_validation(password)
