def grades(a):
    if 2.00 <= a <= 2.99:
        return 'Fail'
    elif 3.00 <= a <= 3.99:
        return 'Poor'
    elif 4.00 <= a <= 5.99:
        return 'Good'
    elif 5.00 <= a <= 5.99:
        return 'Very Good'
    else:
        return 'Excellent'


grade = float(input())

print(grades(grade))
