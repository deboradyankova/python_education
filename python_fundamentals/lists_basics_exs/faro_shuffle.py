deck = input().split()
shuffle = int(input())

first_card = deck.pop(0)
last_card = deck.pop()

first_deck = deck[:len(deck)//2]
sec_deck = deck[len(deck)//2:]


for _ in range(shuffle):
    new_deck = []
    shaked = list(zip(sec_deck, first_deck))
    for pair in shaked:
        card1, card2 = pair
        new_deck.append(card1)
        new_deck.append(card2)
    first_deck = new_deck[:len(deck)//2]
    sec_deck = new_deck[len(deck)//2:]

print(first_deck)
print(sec_deck)

