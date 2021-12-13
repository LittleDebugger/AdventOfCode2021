import re

file = [line.strip() for line in open("input.txt")]

points = set()

for i in range(len(file)):
    if file[i] == '':
        break
    s = file[i].split(',')
    x = int(s[0])
    y = int(s[1])

    points.add((x, y))

for i in range(i + 1, len(file)):
    s = re.split('[ =]', file[i])

    if s[2] == 'x':
        fold = int(s[3])
        adds = []

        for point in points:
            x = fold - abs(fold - point[0])
            adds.append((x, point[1]))

        points = set()

        for r in adds:
            points.add(r)

    else:
        fold = int(s[3])
        adds = []

        for point in points:
            y = fold - abs(fold - point[1])
            adds.append((point[0], y))

        points = set()

        for r in adds:
            points.add(r)


for y in range(10):
    for x in range(60):
        print('*' if (x, y) in points else ' ', end='')
    print('')
