n_jury = int(input())

grade_counter = 0
sum_grade = 0

while True:
    problem_name = input()

    if problem_name == 'Finish':
        average_grade = sum_grade / grade_counter
        print(f' Student \'s final assessment is {average_grade:.2f}')
        break

    current_grade_counter = 0

    for x in range(n_jury):
        grade = float(input())
        grade_counter += 1
        sum_grade += grade
        current_grade_counter += grade

    current_average_grade = current_grade_counter / n_jury
    print(f'{problem_name} - {current_average_grade:.2f}')


