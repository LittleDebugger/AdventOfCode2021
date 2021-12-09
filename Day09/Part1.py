file = [[int(c) for c in line.strip()] for line in open("input.txt")]

total = 0
row = 0
for line in file:
    for c in range(0, len(line)):

        left = 100000 if c == 0 else line[c - 1]
        right = 100000 if c == len(line) - 1 else line[c + 1]
        top = 100000 if row == 0 else file[row - 1][c]
        bottom = 100000 if row > len(file) - 2 else file[row + 1][c]

        if line[c] < left and line[c] < right and line[c] < bottom and line[c] < top:
            total += line[c] + 1
    row = row + 1

print(total)

