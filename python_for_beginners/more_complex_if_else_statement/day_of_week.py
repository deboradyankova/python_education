# number = int(input('Day of week'))
#
# if 1 <= number <= 7:
#     if number == 1:
#         print("Monday")
#     elif number == 2:
#         print("Tuesday")
#     elif number == 3:
#         print("Wednesday")
#     elif number == 4:
#         print("Thursday")
#     elif number == 5:
#         print("Friday")
#     elif number == 6:
#         print("Saturday")
#     elif number == 7:
#         print("Sunday")
# else:
#     print("Error")

days = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday',
}

day = int(input('day of week'))

if day in days.keys():
    print(days[day])




