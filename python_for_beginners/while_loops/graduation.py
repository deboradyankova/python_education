name = input('name')

excluded = 0
class_year = 1
grades_sum = 0

while True:

    if excluded > 1:
        break
    if class_year > 12:
        break

    grade = float(input())

    if grade >= 4:
        class_year += 1
        grades_sum += grade
    else:
        excluded += 1

if excluded > 1:
    print(f'{name} is excluded!')
else:
    average_grade = grades_sum / 12
    print(f'{name} has graduated with av. {average_grade:.2f}')


