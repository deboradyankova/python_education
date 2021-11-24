from pandas import eval

n1 = input('N1')
n2 = input('N2')
operator = input('operator')

equation = f'{n1} {operator} {n2}'

result = eval(equation)

if result.__str__() == 'inf':
    print(f'Cannot divide {n1} by zero')
else:
    if result % 2 == 0:
        equation += f' = {result} - even'
    else:
        equation += f' = {result} - odd'

    print(equation)
