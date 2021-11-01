age = float(input('age'))
gender = input('gender')
bike = input('bike')

if gender == 'm':
    if age >= 16:
        print("Mr")
    else:
        print("Master")
else:
    if age < 16:
        print("Miss")
    else:
        print('Ms')


# gender_type = ''
#
# if age >= 16 and gender == 'm':
#     gender_type = 'Mr'
# elif age < 16 and gender == 'm':
#     gender_type = 'Master'
# elif age >= 16 and gender == 'f':
#     gender_type = 'Ms.'
# elif age < 16 and gender == 'f':
#     gender_type = 'Miss'

# print(gender_type)

# example_2

# age = float(input('age'))
# gender = input('gender')
#
# if age >= 16 and gender == 'm':
#     print('Mr')
# elif age < 16 and gender == 'm':
#     print('Master')
# elif age >= 16 and gender == 'f':
#     print('Ms')
# elif age < 16 and gender == 'f':
#     print('Miss')
