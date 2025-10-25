import numpy as np

file = [line.strip() for line in open("input.txt")]

newFile = file[:3]
newFile.append(file[3])
newFile.append(file[4])
file = newFile

homeSize = len(file) - 4


class Pod:
    type = None


width = 11
a = 2
b = 4
c = 6
d = 8

cols = dict()
cols['A'] = 2
cols['B'] = 4
cols['C'] = 6
cols['D'] = 8

row = dict()
for i in range(11):
    row[i] = None
pods = []
homes = dict()
homes['A'] = 2
homes['B'] = 4
homes['C'] = 6
homes['D'] = 8

types = ['A', 'B', 'C', 'D']
stops = [0, 1, 3, 5, 7, 9, 10]
scores = dict()
scores['A'] = 1
scores['B'] = 10
scores['C'] = 100
scores['D'] = 1000

bestHistory = []

grid = []
for i in range(homeSize + 2):
    grid.append([' ' for x in range(11)])

depth = 1

for line in file[2:-1]:
    # print(line)
    i = 2
    for c in line:
        if c.isalpha():
            grid[depth][i] = c
            i += 2
    depth += 1


def copyGrid(grid):
    copyGrid = []
    for g in range(len(grid)):
        copyGrid.append(grid[g][:])
    return copyGrid


bestScore = 1000000000


def moveToHomeFromHallway(grid, pod, column):
    global cols, homeSize
    homeColumn = cols[pod]

    for g in grid[1:]:
        if g[homeColumn] != ' ' and g[homeColumn] != pod:
            return - 1

    hallwayToHallway = moveToHallwayFromHallway(grid, pod, column, homeColumn)
    if hallwayToHallway == -1:
        return -1

    score = scores[pod]
    total = score

    for g in grid[1:]:
        if g[homeColumn] == ' ':
            total += score
    total += hallwayToHallway

    return total


def moveToHallwayFromRoom(grid, pod, column, depth, targetColumn):
    score = depth * scores[pod]

    if column == targetColumn:
        return score

    s = moveToHallwayFromHallway(grid, pod, column, targetColumn)
    if s == -1:
        return -1

    score += s
    return score


def moveToHallwayFromHallway(grid, pod, column, targetColumn):
    for i in range(targetColumn, column, 1 if column > targetColumn else -1):
        if grid[0][i] != ' ':
            return -1
    return abs(column - targetColumn) * scores[pod]


def moveToHomeFromRoom(grid, pod, column, depth):
    if column == homes[pod]:
        return -1

    s = moveToHallwayFromRoom(grid, pod, column, depth, column)
    if s == -1:
        return -1
    t = s
    s = moveToHomeFromHallway(grid, pod, column)

    if s == -1:
        return -1
    return t + s


def putPodInHome(grid, pod):
    home = homes[pod]
    for i in range(homeSize + 1, 0, -1):
        if grid[i][home] == ' ':
            grid[i][home] = pod
            if i == 1:
                return True
            return False


goes = 0
q = []

q.append((grid, [2, 4, 6, 8], 0, grid, 0, []))

visited = dict()


def printGrid(grid):
    for i in range(len(grid)):
        print(''.join(['.' if x == ' ' else x for x in grid[i]]))


printGrid(grid)
# exit()

while len(q) > 0:
    # print(goes)
    gridStart, sideRoomsStart, score, previousGrid, oldScore, hist = q.pop()
    histCopy = hist[:]
    histCopy.append(gridStart)
    hash = ''
    for i in range(homeSize + 2):
        hash += ''.join(gridStart[i])
    if hash in visited and visited[hash] <= score:
        continue

    visited[hash] = score

    goes += 1

    if score > bestScore:
        continue

    for i in range(11):

        pod = gridStart[0][i]
        if pod != ' ':
            s = moveToHomeFromHallway(gridStart, pod, i)
            if s > -1:
                newScore = score + s
                grid = copyGrid(gridStart)
                grid[0][i] = ' '
                homeDone = putPodInHome(grid, pod)
                sideRooms = sideRoomsStart[:]
                if homeDone:
                    # print('no more side rooms')
                    # exit()
                    # print(np.array(grid))
                    sideRooms.remove(homes[pod])
                    # print(len(sideRooms))
                    if len(sideRooms) == 0:
                        if newScore < bestScore:
                            bestScore = newScore
                            bestHistory = hist
                            print(bestScore)
                        continue
                q.append((grid, sideRooms, newScore, gridStart, score, histCopy))

    for i in range(2, 11, 2):
        if i not in sideRoomsStart:
            continue

        for depth in range(1, homeSize + 2):

            pod = gridStart[depth][i]
            if pod == ' ':
                continue
            # move to room
            toRoomScore = moveToHomeFromRoom(gridStart, pod, i, depth)
            if toRoomScore > -1:
                newScore = score + toRoomScore
                grid = copyGrid(gridStart)
                grid[depth][i] = ' '
                homeDone = putPodInHome(grid, pod)
                sideRooms = sideRoomsStart[:]
                if homeDone:
                    sideRooms.remove(homes[pod])
                    if len(sideRooms) == 0:
                        if newScore < bestScore:
                            bestScore = newScore
                            bestHistory = hist
                            print(bestScore)
                        continue
                q.append((grid, sideRooms, newScore, gridStart, score, histCopy))

            # move to hall
            for space in stops:
                toSpaceScore = moveToHallwayFromRoom(gridStart, pod, i, depth, space)
                if toSpaceScore == -1:
                    continue
                newScore = score + toSpaceScore
                grid = copyGrid(gridStart)
                grid[depth][i] = ' '
                grid[0][space] = pod
                sideRooms = sideRoomsStart[:]

                q.append((grid, sideRooms, newScore, gridStart, score, histCopy))
            break

print(bestScore)
print('here')
print(goes)

for i in bestHistory:
    print('******************************************')
    printGrid(i)
