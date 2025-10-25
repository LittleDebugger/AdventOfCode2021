import re

file = [line.strip() for line in open("input.txt")]

co = []

rMinX = 0
rMaxX = 0
rMinY = 0
rMaxY = 0
rMinZ = 0
rMaxZ = 0

xs = set()
ys = set()
zs = set()
for line in file:

    l = re.split(' |=|,|\.', line)
    on = 1 if l[0] == 'on' else 0
    minX = int(l[2])
    maxX = int(l[4])
    minY = int(l[6])
    maxY = int(l[8])
    minZ = int(l[10])
    maxZ = int(l[12])

    xs.add(minX)
    ys.add(minY)
    zs.add(minZ)

    xs.add(maxX + 1)
    ys.add(maxY + 1)
    zs.add(maxZ + 1)

    if minX < rMinX:
        rMinX = minX
    if maxX > rMaxX:
        rMaxX = maxX
    if minY < rMinY:
        rMinY = minY
    if maxY > rMaxY:
        rMaxY = maxY
    if minZ < rMinZ:
        rMinZ = minZ
    if maxZ > rMaxZ:
        rMaxZ = maxZ

vol = 0

zsList = list(zs)
zsList.sort()
ysList = list(ys)
ysList.sort()
xsList = list(xs)
xsList.sort()

print(vol)

total = 0

done = set()


def getRange(l, m, mm):
    ii = len(l) // 2
    i = 0
    while True:

        if l[i + ii] < m:
            i += ii
        else:
            ii = ii // 2
            if ii == 0:
                break
    rv = []
    for ii in range(i, len(l)):
        # print(ii)
        if l[ii] >= m and l[ii] <= mm:
            rv.append(ii)
        elif l[ii] > mm:
            return rv

    return rv


file.reverse()
i = 0

completed = []

for line in file:
    l = re.split(' |=|,|\.', line)
    print(i, len(file))
    i += 1
    on = True if l[0] == 'on' else False

    minX = int(l[2])
    maxX = int(l[4])
    minY = int(l[6])
    maxY = int(l[8])
    minZ = int(l[10])
    maxZ = int(l[12])

    withIn = [x for x in completed if
              minX >= x[0] and maxX <= x[1] and minY >= x[2] and maxY <= x[3] and minZ >= x[4] and maxZ <= x[5]]
    if len(withIn) > 0:
        continue

    completed.append((minX, maxX, minY, maxY, minZ, maxZ))

    goodZs = getRange(zsList, minZ, maxZ)
    goodYs = getRange(ysList, minY, maxY)
    goodXs = getRange(xsList, minX, maxX)

    for goodZ in goodZs:
        for goodY in goodYs:
            for goodX in goodXs:
                area = (goodZ, goodY, goodX)
                if area in done:
                    continue

                if on: \
                        total += (abs(xsList[goodX + 1] - xsList[goodX])) * (abs(ysList[goodY + 1] - ysList[goodY])) * (
                            abs(zsList[goodZ + 1] - zsList[goodZ]))

                done.add(area)
print(total)
