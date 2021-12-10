favourite_book = input()
checked_books = 0
found_book = False

while True:
    current_book = input()
    if current_book == 'No More Books':
        break
    if current_book == favourite_book:
        found_book = True
        break
    checked_books += 1

if found_book:
    print(f'You checked {checked_books} and you found it')
else:
    print("The book you search is not here!")
    print(f'You checked {checked_books} books.')
