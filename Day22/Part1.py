import re

file = [line.strip() for line in open("input.txt")]

co = []

for z in range(-50, 50 + 1):
    square = []
    co.append(square)
    for y in range(-50, 50 + 1):
        row = []
        square.append(row)
        for x in range(-50, 50 + 1):
            row.append(0)

for line in file:
    l = re.split(' |=|,|\.', line)
    print(l)
    on = 1 if  l[0] == 'on' else 0
    minX = int(l[2])
    maxX = int(l[4])
    minY = int(l[6])
    maxY = int(l[8])
    minZ = int(l[10])
    maxZ = int(l[12])
    if  minX > 50 or minX < -50 or minY > 50 or minY < -50 or minZ > 50 or minZ < -50 or maxX > 50 or maxX < -50 or maxY > 50 or maxY < -50 or maxZ > 50 or maxZ < -50:
        continue

    for zz in range(minZ, maxZ + 1):
        for yy in range(minY, maxY + 1):
            for xx in range(minX, maxX + 1):
                co[zz][yy][xx] = on

t = 0
for zz in range(-50, 50 + 1):
    for yy in range(-50, 50 + 1):
        for xx in range(-50, 50 + 1):
            if co[zz][yy][xx] == 1:
                t += 1

print(t)
