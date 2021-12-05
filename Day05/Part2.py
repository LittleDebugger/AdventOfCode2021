import re

file = [line.strip() for line in open("input.txt")]

grid = []
length = 1000

for b in range(0, length):
    grid.append([0 for a in range(0, length)])

for line in file:
    splitLine = re.split(' |-|>|,', line)

    x1 = int(splitLine[0])
    y1 = int(splitLine[1])
    x2 = int(splitLine[5])
    y2 = int(splitLine[6])

    if x1 == x2 or y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                grid[y][x] = grid[y][x] + 1
    else:
        diff = max(x1, x2) + 1 - min(x1, x2)

        xOffset = 1 if x1 < x2 else -1
        yOffset = 1 if y1 < y2 else -1
        for co in range(0, diff):
            grid[y1 + (yOffset * co)][x1 + (xOffset * co)] = grid[y1 + (yOffset * co)][x1 + (xOffset * co)] + 1

total = 0
for x in range(0, length):
    for y in range(0, length):
        if grid[x][y] > 1:
            total += 1

print(total)
