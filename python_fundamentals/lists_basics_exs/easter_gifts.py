def out_of_stock(gifts_list, gift):
    count = gifts_list.count(gift)
    for _ in range(count):
        index = gifts_list.index(gift)
        gifts_list[index] = None
    return gifts_list

def required(gifts_list,*args):
    gift, index = args
    if int(index) < len(gifts_list):
        gifts_list[int(index)] = gift
    return gifts_list

def just_in_case(gifts_list, gift):
    gifts_list[-1] = gift
    return gifts_list

gifts = input().split()

while True:
    line = input()
    if line == 'No Money':
        break

    command, *args = line.split()

    if command == 'OutOfStock':
        gifts = out_of_stock(gifts, args[0])
    elif command == 'Required':
        gifts = required(gifts, *args)
    else:
        gifts = just_in_case(gifts, args[0])

gifts = [x for x in gifts if x]
print(' '.join(gifts))
