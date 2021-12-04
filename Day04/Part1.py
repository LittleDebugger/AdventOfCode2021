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


for number in numbers:
    for card in cards:
        for rowIndex in range(0, length):
            for colIndex in range(0, length):
                if card[rowIndex][colIndex] == number:
                    card[rowIndex][colIndex] = done

    for card in cards:
        # little bit of duplication in here
        for rowIndex in range(0, length):
            rowTotal = sum(map(lambda x: x[rowIndex], card))
            if rowTotal == done * length:
                print(get_answer(card, number))
                exit()
        for colIndex in range(0, length):
            colTotal = sum(card[colIndex])
            if colTotal == done * length:
                print(get_answer(card, number))
                exit()
