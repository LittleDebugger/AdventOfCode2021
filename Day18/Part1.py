import math

file = [line.strip() for line in open("input.txt")]


class Squid:
    vals = None
    parent = None
    position = None

    def __str__(self):
        return '[' + repr(self) + ']'

    def __repr__(self):
        return ','.join(str(val) for val in self.vals)


pos = 1
line = None


def go(parent):
    global pos, line
    squid = Squid()
    squid.vals = []
    squid.parent = parent
    squid.position = len(parent.vals) if parent is not None else 0

    num = ''
    while pos < len(line):
        char = line[pos]
        pos += 1
        if char == '[':
            squid.vals.append(go(squid))
        if char == ']':
            if len(num) > 0:
                squid.vals.append(int(num))
            return squid
        if char == ',':
            if len(num) > 0:
                squid.vals.append(int(num))
            num = ''
        if char.isnumeric():
            num += char
    return squid


def addRight(squid, num):
    while True:
        if isinstance(squid.vals[1], int):
            squid.vals[1] += num
            return
        else:
            squid = squid.vals[1]


def addLeft(squid, num):
    while True:
        if isinstance(squid.vals[0], int):
            squid.vals[0] += num
            return
        else:
            squid = squid.vals[0]


def addPrevious(squid, i, num):
    if i == 1:
        if isinstance(squid.vals[0], int):
            squid.vals[0] += num
            return
        else:
            addRight(squid.vals[0], num)

    else:
        if squid.parent is not None:
            addPrevious(squid.parent, squid.position, num)


def addNext(squid, i, num):
    if i == 0:
        if isinstance(squid.vals[1], int):
            squid.vals[1] += num
            return
        else:
            addLeft(squid.vals[1], num)

    else:
        if squid.parent != None:
            addNext(squid.parent, squid.position, num)


def checkDepth(squid, depth):
    if depth == 4:
        addPrevious(squid.parent, squid.position, squid.vals[0])
        addNext(squid.parent, squid.position, squid.vals[1])
        squid.parent.vals[squid.position] = 0
        return True
    else:
        for i in range(2):
            next = squid.vals[i]
            if isinstance(next, int) == False:
                r = checkDepth(next, depth + 1)
                if r:
                    return True
    return False


def test(squid, depth):
    for i in range(2):
        next = squid.vals[i]
        if isinstance(next, int):
            if next >= 10:
                newSquid = Squid()
                newSquid.parent = squid
                newSquid.position = i
                newSquid.vals = [next // 2, math.ceil(next / 2)]
                squid.vals[i] = newSquid
                return True
        else:
            r = test(next, depth + 1)
            if r:
                return True
    return False


def getVal(squid):
    val = 0
    for i in range(2):
        next = squid.vals[i]
        val += (next if isinstance(next, int) else getVal(next)) * (3 if i == 0 else 2)
    return val


start = None
for nextPart in file:
    pos = 1
    if line is None:
        line = nextPart
    else:
        line = '[' + line + ',' + nextPart + ']'

    start = go(None)
    cont = True
    while cont:
        cont = checkDepth(start, 0)
        if cont:
            continue
        cont = test(start, 0)
    line = str(start)

print(getVal(start))
