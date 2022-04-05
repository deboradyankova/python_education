lst_nums = input().split(', ')

lst_nums = [int(n) for n in lst_nums]
count_of_zeros = lst_nums.count(0)

for _ in range(count_of_zeros):
    lst_nums.remove(0)
    lst_nums.append(0)

print(lst_nums)
