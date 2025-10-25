import re

input = "target area: x=257..286, y=-101..-57"
bits = re.split(' |\.|=|,', input)

print(bits)

print(bits[3],bits[5],bits[7], bits[9])

minX = int(bits[3])
maxX = int(bits[5])
minY = int(bits[8])
maxY = int(bits[10])

x = 0
y = 0

xc = 0
xy = 0

bestX = 1000000000000
bestY = 1000000000000
bestHighy = 0

t = 0
maxXc = 0
t = set()

def check(xc, xy):
    global t, bestHighy, highY, bestX, bestY, minX, minY, minX, maxY, maxXc,t
    x = 0
    y = 0
    i = 0
    highY = 0
    done = False
    while x <= maxX and y >= minY and not done:
        if y > highY:
            highY = y
        if x >= minX and x <= maxX and y >= minY and y <= maxY:
            if xc < bestX:
                bestX = xc
            if yc < bestY:
                bestY = yc
            if highY > bestHighy:
                bestHighy = highY
            if xc > maxXc:
                maxXc = xc
            done = True
            t.add((xc,yc))
            continue
        x += max(0, xc - i)
        y += yc - i
        i += 1


for xc in range(1, 300):
    for yc in range(-102, 250):
        check(xc, xy)

print("step1", len(t))
for a in range(0, 1000000):
    check(23, a)
    if a % 100 == 0:
        print(len(t))

print(bestX, bestY, bestHighy)
print(len(t), maxXc)