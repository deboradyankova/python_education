row = int(input())

# for i in range(row):
#     for j in range(i + 1):
#         print('*', end=' ')
#     print('\r')
# for k in range(row - 1, 0, -1):
#     for l in range(k, 0, -1):
#         print('*', end=' ')
#     print('\r')

for positive_row in range(1, row + 1):
    print('*'*positive_row)
for negative_row in range(row - 1, -1, -1):
    print('*'*negative_row)
