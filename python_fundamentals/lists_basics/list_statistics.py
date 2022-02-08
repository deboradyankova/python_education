n = int(input())

lst_positive = []
lst_negative = []

for _ in range(n):
    number = int(input())
    if number >= 0:
        lst_positive.append(number)
    else:
        lst_negative.append(number)
print(lst_positive)
print(lst_negative)
print(f'Count of positives: {len(lst_positive)}. Sum of negatives: {sum(lst_negative)}')

