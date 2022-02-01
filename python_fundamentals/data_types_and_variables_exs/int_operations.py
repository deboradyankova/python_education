from math import trunc

first_num = int(input())
second_num = int(input())
third_number = int(input())
forth_number = int(input())

operations = ((first_num + second_num) / third_number) * forth_number
print(trunc(operations))
