file = [[int(a) for a in line.strip()] for line in open("input.txt")]

t = 0
width = len(file[0])
height = len(file)


def increase(x, y):
    if x < 0 or y < 0 or x >= width or y >= height:
        return

    if file[y][x] == -1:
        return

    file[y][x] += 1

    if file[y][x] >= 10:
        file[y][x] = -1
        increase(x + 1, y)
        increase(x - 1, y)
        increase(x, y + 1)
        increase(x, y - 1)

        increase(x + 1, y - 1)
        increase(x - 1, y - 1)
        increase(x + 1, y + 1)
        increase(x - 1, y + 1)


for i in range(1, 10000000000000):
    t = 0
    for y in range(height):
        for x in range(width):
            increase(x, y)

    for y in range(height):
        for x in range(width):
            if file[y][x] == -1:
                t += 1
                file[y][x] = 0

    if t == width * height:
        print(i)
        exit()
