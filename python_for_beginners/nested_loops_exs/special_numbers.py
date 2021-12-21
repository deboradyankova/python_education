special_number = int(input())

for n_1 in range(1, 10):
    for n_2 in range(1, 10):
        for n_3 in range(1, 10):
            for n_4 in range(1, 10):

                if special_number % n_1 == 0 \
                        and special_number % n_2 == 0 \
                        and special_number % n_3 == 0 \
                        and special_number % n_4 == 0:
                    print(f'{n_1}{n_2}{n_3}{n_4}', end=' ')
