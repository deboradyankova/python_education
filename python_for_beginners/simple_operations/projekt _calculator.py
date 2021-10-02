NEEDED_TIME_PER_PROJECT = 3

architect_name = input('Architect name: ')
number_of_projects = int(input("number of projects: "))
number_of_projects = abs(number_of_projects)
total_hours = number_of_projects * NEEDED_TIME_PER_PROJECT

output = f"The architect {architect_name} will need {total_hours} hours to complete {number_of_projects} project/s."
print(output)
