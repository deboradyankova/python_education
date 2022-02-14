nums_lst =[int(n) for n in input().split()]
count_of_num_to_remove = int(input())

for _ in range(count_of_num_to_remove):
    nums_lst.remove(min(nums_lst))
print(nums_lst)

