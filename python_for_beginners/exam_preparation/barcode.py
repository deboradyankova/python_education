first_num = input()
sec_num = input()

index = 0

for i in range(int(first_num[index]), int(sec_num[index])+1):
    for j in range(int(first_num[index + 1]), int(sec_num[index + 1]) + 1):
        for k in range(int(first_num[index + 2]), int(sec_num[index + 2]) + 1):
            for l in range(int(first_num[index + 3]), int(sec_num[index + 3]) + 1):
                if i % 2 != 0 and j % 2 != 0 and k % 2 != 0 and l % 2 != 0:
                    print(f'{i}{j}{k}{l}', end=' ')



