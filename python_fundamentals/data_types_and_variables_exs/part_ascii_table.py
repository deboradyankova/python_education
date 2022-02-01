import random

char_start = int(input())
char_end = int(input())

for symbol in range(char_start, char_end + 1):
    print(chr(symbol), end=' ')

