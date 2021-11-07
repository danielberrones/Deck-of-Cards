from random import choice, shuffle

suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
rank = ['Ace','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King']
deck = []
values = rank[0]

shuffle(suits)
shuffle(rank)

while rank:
    try:
        r = rank.pop()
        s = choice(suits)
        print(r+ ' of ' + s)
    except IndexError:
        pass

