file = [line.strip() for line in open("input.txt")]

numbers = [int(a) for a in file[0].split(',')]
cards = []

# number larger than any on the cards
done = 1000000

# count of numbers in a row/column
length = 5

for i in range(1, len(file)):
    if file[i] == '':
        card = []
        cards.append(card)
        continue
    card.append([int(a) for a in file[i].split()])


def get_answer(grid, last_called_number):
    total = 0
    for rowIx in range(0, length):
        for colIx in range(0, length):
            if grid[rowIx][colIx] != done:
                total += grid[rowIx][colIx]
    return total * last_called_number


remainingCards = [a for a in range(0, len(cards))]

# This is actually buggy and only works because I forgot that Python does not exit when exit() is called within a try
# block (which I only found out a few days ago). So this runs forever but the last console output is the correct answer.
while True:

    for n in numbers:
        for cardIx in remainingCards:
            card = cards[cardIx]
            for rowIx in range(0, length):
                for colIx in range(0, length):
                    if card[rowIx][colIx] == n:
                        card[rowIx][colIx] = done

        for cardIx in range(0, len(cards)):
            card = cards[cardIx]
            # the duplication is a bit worse now than in part 1
            for rowIx in range(0, length):
                rowIx = sum(map(lambda x: x[rowIx], card))
                if rowIx == done * 5:
                    # Exception would be thrown if a attempt is made to remove a card twice. This would happen if a
                    # number filled a row and column. Swallowing the exception was quicker to code than breaking from
                    # the current loop and then continuing on the outer loop. (see comment on the while statement above)
                    try:
                        if len(remainingCards) == 0:
                            print(get_answer(cards[remainingCards[0]], n))
                            exit()
                        remainingCards.remove(cardIx)
                    except:
                        pass

            for colIx in range(0, length):
                colIx = sum(card[colIx])
                if colIx == done * length:
                    try:
                        if len(remainingCards) == 1:
                            print(get_answer(cards[remainingCards[0]], n))
                            exit()
                        remainingCards.remove(cardIx)
                    except:
                        pass
