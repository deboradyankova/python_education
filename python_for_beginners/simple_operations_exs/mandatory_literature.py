number_pages_book = int(input('Number of pages current book'))
pages_one_hour = int(input('Number of pages one hour'))
number_of_days_book = int(input('Number of days for one book'))

total_days_book = number_pages_book // number_of_days_book
total_hours_book = total_days_book // pages_one_hour

print(total_hours_book)
