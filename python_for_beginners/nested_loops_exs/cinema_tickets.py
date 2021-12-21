standard_tickets = 0
student_tickets = 0
kid_tickets = 0

finished = False

while not finished:

    movie = input()

    seats = int(input())
    capacity = seats
    while True:
        ticket = input()
        if ticket == 'Finish' or ticket == 'End':
            if ticket == 'Finish':
                finished = True
            cap_percentage = 100 * seats / capacity
            print(f'{movie} - {100 - cap_percentage:.2f}% full.')
            break

        if ticket == 'standard':
            standard_tickets += 1
        elif ticket == 'student':
            student_tickets += 1
        else:
            kid_tickets += 1

        seats -= 1
        if seats == 0:
            print(f'{movie} - 100% full.')
            finished = True
            break


total_tickets = student_tickets + standard_tickets + kid_tickets

print(f'Total tickets: {total_tickets}')
print(f'{(student_tickets / total_tickets * 100):.2f}% student tickets.')
print(f'{(standard_tickets / total_tickets * 100):.2f}% standard tickets.')
print(f'{(kid_tickets / total_tickets * 100):.2f}% kids tickets.')
