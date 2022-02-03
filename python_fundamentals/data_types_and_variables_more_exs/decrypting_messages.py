key = int(input())
n_lines = int(input())

decrypted = []

for _ in range(n_lines):
    character = input()
    decrypted.append(ord(character) + key)

# result = []
# for ascii_number in decrypted:
#     result.append(chr(ascii_number))
#
# print(''.join(result))


decrypted = [chr(ascii_n) for ascii_n in decrypted]
print(''.join(decrypted))

