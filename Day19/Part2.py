import math

total = 0
file = [line.strip() for line in open("input.txt")]


class beacon():
    id = None
    positions = None

    def __repr__(self):
        return '(beacon: id: %s, %s)' % (self.id, self.position)


class scanner():
    id = None
    beacons = None

    def __repr__(self):
        return '(scanner: id: %s, %s)' % (self.id, self.beacons)


#### parse
scanners = []
scannersLookup = dict()
s = scanner()
s.beacons = []
sId = 0
bId = 0
s.id = sId

totalBeaconCount = 0


def rotateZ(pos):
    newPos = (-pos[1], pos[0], pos[2])
    return newPos


def rotateY(pos):
    newPos = (-pos[2], pos[1], pos[0])
    return newPos


def rotateX(pos):
    newPos = (pos[0], -pos[2], pos[1])
    return newPos


def getPositions(pos):
    positions = []
    positions.append(pos)

    for i in range(4):
        pos = rotateZ(pos)
        positions.append(pos)
        pos = rotateZ(pos)
        positions.append(pos)
        pos = rotateZ(pos)
        positions.append(pos)
        pos = rotateZ(pos)
        positions.append(pos)

        pos = rotateY(pos)

    for i in range(2):
        pos = rotateX(pos)

        positions.append(pos)
        pos = rotateZ(pos)
        positions.append(pos)
        pos = rotateZ(pos)
        positions.append(pos)
        pos = rotateZ(pos)
        positions.append(pos)

        pos = rotateX(pos)

    return positions


for line in file:
    if line.startswith('--'):
        bId = 0
        s = scanner()
        s.beacons = []
        s.id = sId
        sId += 1
        scanners.append(s)
        scannersLookup[s.id] = s
        continue

    if line == '':
        continue

    sl = line.split(',')
    b = beacon()
    b.nodes = []
    b.id = bId
    bId += 1

    b.position = (int(sl[0]), int(sl[1]), int(sl[2]))
    b.offsets = getPositions(b.position)

    s.beacons.append(b)
    b.check = []
    total += 1

print(scannersLookup)

nextI = 0


def addPosition(beacon, pos):
    global nextI
    if len(beacon.positions) == nextI:
        beacon.positions.append([])
    beacon.positions[nextI].append(pos)
    nextI += 1


for scanner in scanners:

    for beacon in scanner.beacons:
        beacon.positions = []
        for beacon2 in scanner.beacons:
            nextI = 0
            pos = ((beacon2.position[0] - beacon.position[0]), (beacon2.position[1] - beacon.position[1]),
                   (beacon2.position[2] - beacon.position[2]))
            for pos in getPositions(pos):
                addPosition(beacon, pos)

all = set()
added = []

yyy = 0


def reduceScannerPositon(scanner, pos):
    print('pos is ', pos)
    for b in scanner.beacons:
        b.positions = b.positions[pos:pos + 1]
        b.offset = b.offsets[pos]


def addAbsPositions(scanner):
    global all, yyy
    if scanner.id in added:
        return

    added.append(scanner.id)
    beacon = scanner.beacons[0]
    for position in beacon.positions[0]:
        ad = ((scanner.offset[0] + position[0] + beacon.offset[0] - beacon.positions[0][0][0]),
              (scanner.offset[1] + position[1] + beacon.offset[1] - beacon.positions[0][0][1]),
              (scanner.offset[2] + position[2] + beacon.offset[2] - beacon.positions[0][0][2]))
        print(ad)

        all.add(ad)

    yyy += 1
    if yyy == 2:
        print(all)
        exit()
        print('*******************')


def setScannerOffset(scanner, beacon, refScanner, refBeacon):
    if hasattr(scanner, 'offset'):
        return

    scanner.offset = (
        refScanner.offset[0] + refBeacon.offset[0] - beacon.offset[0],
        refScanner.offset[1] + refBeacon.offset[1] - beacon.offset[1],
        refScanner.offset[2] + refBeacon.offset[2] - beacon.offset[2],
    )


def reduceScanner(scanner, beacon, pos, refScanner, refBeacon):
    global yyy
    yyy += 2

    if yyy == 1:
        print(all)
        exit()
    reduceScannerPositon(scanner, pos)
    setScannerOffset(scanner, beacon, refScanner, refBeacon)
    addAbsPositions(scanner)


doNext = []
doNext.append(scanners[0])
scannersLeft = scanners[:]

sub = 0

tt = 0

scanners[0].offset = (0, 0, 0)
reduceScannerPositon(scanners[0], 0)
addAbsPositions(scanners[0])

dones = set()

while len(doNext) > 0:
    s1 = doNext.pop()

    scannersLeft.remove(s1)

    bestForThis = 0
    for s2 in scannersLeft:

        done = False
        for b1 in s1.beacons:
            for b2 in s2.beacons:
                matchedZero = False
                for p in range(len(b2.positions)):
                    done = False

                    for pp in b1.positions:

                        t = 0
                        s2Pos = b2.positions[p][:]
                        # print(pp)
                        for p1 in pp:

                            if p1 in s2Pos:
                                # print(s2Pos)
                                # exit()
                                if p1 == (0, 0, 0):
                                    matchedZero = True
                                s2Pos.remove(p1)
                                t += 1

                        if t >= 12 and matchedZero and (0, 0, 0) not in s2Pos:

                            sub += t
                            tt += 1

                            done = True
                            if s2 not in doNext:
                                doNext.append(s2)
                                reduceScanner(s2, b2, p, s1, b1)
                            pass
                        else:
                            pass
                        if done:
                            break
                    if done:
                        break
                if done:
                    break
            if done:
                break

print(total, sub)
print(total - sub)

print('left:', len(scannersLeft))
print('answer', len(all))

best = 0

for a in scanners:
    for b in scanners:
        t = abs(a.offset[0] - b.offset[0]) + abs(a.offset[1] - b.offset[1]) + abs(a.offset[2] - b.offset[2])
        if t > best:
            print('*******')
            print(a)
            print(b)
            print(t)
            best = t

print(all)
