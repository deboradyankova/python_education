number_of_lines = int(input())

open_closed_count = 0
opened = False

for _ in range(number_of_lines):
   line = input()
   if line == '(':
       opened = True
   elif opened and line == ')':
       open_closed_count += 1
       opened = False
   elif line ==')' and not opened:
       break

if open_closed_count and not opened:
    print('BALANCED')
else:
    print('UNBALANCED')




