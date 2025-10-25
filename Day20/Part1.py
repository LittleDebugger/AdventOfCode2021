import numpy as np

file = [line.strip() for line in open("input.txt")]
map = file[0]

image = []

for i in range(2, len(file)):
    image.append([0 if c == '.' else 1 for c in file[i]])

print(np.array(image))

next = 0


width = len(image)
print(width)

cc = 0
for r in range(50):
    width = len(image)
    transImage = []

    for y in range(-2, width + 2):
        line = []
        transImage.append(line)
        for x in range(-2, width + 2):
            point = 0
            s = ''

            s += str(next if (x - 1 < 0 or y - 1 < 0) or (x - 1 >= width or y - 1 >= width) else image[y - 1][x - 1])
            s += str(next if (x < 0 or y - 1 < 0) or (x >= width or y - 1 >= width) else image[y - 1][x])
            s += str(next if (x + 1 < 0 or y - 1 < 0) or (x + 1 >= width or y - 1 >= width) else image[y - 1][x + 1])

            s += str(next if (x - 1 < 0 or y < 0) or (x - 1 >= width or y >= width) else image[y][x - 1])
            s += str(next if (x < 0 or y < 0) or (x >= width or y >= width) else image[y][x])
            s += str(next if (x + 1 < 0 or y < 0) or (x + 1 >= width or y >= width) else image[y][x + 1])

            s += str(next if (x - 1 < 0 or y + 1 < 0) or (x - 1 >= width or y + 1 >= width) else image[y + 1][x - 1])
            s += str(next if (x < 0 or y + 1 < 0) or (x >= width or y + 1 >= width) else image[y + 1][x])
            s += str(next if (x + 1 < 0 or y + 1 < 0) or (x + 1 >= width or y + 1 >= width) else image[y + 1][x + 1])

            cc = 0 if map[int(s, 2)] == '.' else 1
            line.append(cc)

    image = transImage
    print(cc)
    next = cc

    print(np.array(image))

t = 0

for y in range(len(image)):
    for x in range(len(image[0])):
        if image[y][x] == 1:
            t += 1

print(t)