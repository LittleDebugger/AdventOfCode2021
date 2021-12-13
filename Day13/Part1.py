file = [line.strip() for line in open("input.txt")]

points = set()

for i in range(len(file)):
    if file[i] == '':
        break
    s = file[i].split(',')
    x = int(s[0])
    y = int(s[1])

    points.add((x, y))


firstFoldLine = 655
adds = []

for point in points:
    x = firstFoldLine - abs(firstFoldLine - point[0])
    adds.append((x, point[1]))

points = set()

for r in adds:
    points.add(r)

print(len(points))
