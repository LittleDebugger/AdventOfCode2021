import numpy as np

grid = [[c for c in line.strip()] for line in open("input.txt")]

print(np.array(grid))
def copy():
    global  grid
    copyGrid = []
    for y in range(len(grid)):
        row = []
        copyGrid.append(row)
        for x in range(len(grid[0])):
            row.append(grid[y][x])
    return  copyGrid


i = 0
move = True

while(move):
    i += 1
    move = False

    copyGrid = copy()
    for y in range(-1, len(grid) -1):
        for x in range(-1, len(grid[0])- 1):
            if grid[y][x] == '>':
                if grid[y][(x + 1)] == '.':
                    copyGrid[y][(x + 1)] = '>'
                    copyGrid[y][x] = '.'
                    move = True

    grid = copyGrid
    copyGrid = copy()

    for y in range(-1, len(grid) - 1):
        for x in range(-1, len(grid[0]) -1):
            if grid[y][x] == 'v':
                if grid[(y + 1)][x] == '.':
                    copyGrid[(y+1)][x] = 'v'
                    copyGrid[y][x] = '.'
                    move = True


    grid = copyGrid

print(i)