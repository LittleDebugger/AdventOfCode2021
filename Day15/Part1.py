import numpy as np

file = [[int(x) for x in line.strip()] for line in open("input.txt")]

big = 100000000

visits = []
distances = []

width = len(file[0])
height = len(file)

for y in range(height):
    row = []
    for x in range(width):
        row.append(big)
    distances.append(row)

distances[0][0] = 0

changes = True
while changes:
    changes = False
    for y in range(height):
        for x in range(width):
            if x == 0 and y == 0:
                continue

            best = big
            if x > 0:
                if distances[y][x - 1] < best:
                    best = distances[y][x - 1]
            if y > 0:
                if distances[y - 1][x] < best:
                    best = distances[y - 1][x]
            if x < width - 1:
                if distances[y][x + 1] < best:
                    best = distances[y][x + 1]
            if y < height - 1:
                if distances[y + 1][x] < best:
                    best = distances[y + 1][x]

            best = best + file[y][x]

            if best < distances[y][x]:
                distances[y][x] = best
                changes = True

# bottom right distance
print(np.array(distances))
