number_poor_grades = int(input())

poor_grades_counter = 0
solved_problems_counter = 0
grades_sum = 0
last_problem = None

while True:
    exs_name = input()
    if exs_name == 'Enough':
        break

    grade = int(input())

    if grade <= 4:
        poor_grades_counter += 1
        if number_poor_grades == poor_grades_counter:
            break
    else:
        solved_problems_counter += 1
        grades_sum += grade
        last_problem = exs_name

if poor_grades_counter == number_poor_grades:
    print(f'You need a break, {number_poor_grades} poor grades.')
else:
    av_score = grades_sum / solved_problems_counter

    print(
        f'''
        Average score: {av_score:.2f}
        Number of problems: {solved_problems_counter}
        Last problem: {last_problem}
        '''
    )
