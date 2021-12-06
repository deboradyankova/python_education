# lst = ["Sam", "Lisa", "Micha", "Dave", "Wyatt", "Emma", "Sage"]
# for i in lst:
#     print(f'Hello {i}')
#
# name = "Antarctica"
# for i in name:
#     print(i)

# name = "Civilization"
#
# c = 0
# for i in name:
#     c += 1
#     print(c)
nl = []
for x in range(1500, 2701):
    if (x % 7 == 0) and (x % 5 == 0):
        nl.append(str(x))
print(','.join(nl))
