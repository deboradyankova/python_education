COEFFICIENT_SCHOLARSHIP = 25
PERCENT_SOCIAL_SCHOLARSHIP = 0.35
SOCIAL_AVERAGE_SUCCESS = 4.5
EXCELLENT_AVERAGE_SUCCESS = 5.5

income_lev_per_person = float(input('Income'))
average_success = float(input('Average success'))
minimal_salary = float(input('Minimal salary'))

scholarship = None
if income_lev_per_person < minimal_salary and average_success > SOCIAL_AVERAGE_SUCCESS:
    scholarship = minimal_salary * PERCENT_SOCIAL_SCHOLARSHIP

excellent_success_scholarship_per_student = None
if average_success >= EXCELLENT_AVERAGE_SUCCESS:
    excellent_success_scholarship_per_student = average_success * COEFFICIENT_SCHOLARSHIP

if not scholarship and not excellent_success_scholarship_per_student:
    print("You cannot get a scholarship!")
elif scholarship > excellent_success_scholarship_per_student:
    print(f'You get a Social scholarship {scholarship:.2f} BGN')
else:
    print(f'You get a scholarship for excellent results {excellent_success_scholarship_per_student:.2f} BGN')

