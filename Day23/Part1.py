import numpy as np

file = [line.strip() for line in open("input.txt")]

print(file)


class Pod:
    type = None


width = 11  # 11
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

grid = []
grid.append([' ' for x in range(11)])
grid.append([' ' for x in range(11)])
grid.append([' ' for x in range(11)])

depth = 1

for line in file[2:-1]:
    print(line)
    i = 2
    for c in line:
        if c.isalpha():
            grid[depth][i] = c
            i += 2
    depth += 1


def copyGrid(grid):
    copyGrid = []
    copyGrid.append(grid[0][:])
    copyGrid.append(grid[1][:])
    copyGrid.append(grid[2][:])
    return copyGrid


bestScore = 1000000000


def moveToHomeFromHallway(grid, pod, column):
    global cols
    homeColumn = cols[pod]
    if (grid[1][homeColumn] != ' ' and grid[1][homeColumn] != pod) or (
            grid[2][homeColumn] != ' ' and grid[2][homeColumn] != pod):
        return -1

    hallwayToHallway = moveToHallwayFromHallway(grid, pod, column, homeColumn)
    if hallwayToHallway == -1:
        return -1

    score = scores[pod]

    if grid[2][homeColumn] == ' ':
        score += score
    score += hallwayToHallway

    return score


def moveToHallwayFromRoom(grid, pod, column, depth, targetColumn):
    if depth == 2 and grid[1][column] != ' ':
        return -1

    score = depth * scores[pod]

    if column == targetColumn:
        return score

    s = moveToHallwayFromHallway(grid, pod, column, targetColumn)
    if s == -1:
        return -1

    score += s
    if score == 1:
        exit()
    return score


def moveToHallwayFromHallway(grid, pod, column, targetColumn):
    for i in range(targetColumn, column, 1 if column > targetColumn else -1):
        if grid[0][i] != ' ':
            return -1

    return abs(column - targetColumn) * scores[pod]


def moveToHomeFromRoom(grid, pod, column, depth):
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
    if grid[2][home] == ' ':
        grid[2][home] = pod
        return False
    grid[1][home] = pod
    return True


goes = 0
q = []

q.append((grid, [2, 4, 6, 8], 0, grid, 0))

visited = dict()


def printGrid(grid):
    print(''.join(['.' if x == ' ' else x for x in grid[0]]))
    print(''.join(['.' if x == ' ' else x for x in grid[1]]))
    print(''.join(['.' if x == ' ' else x for x in grid[2]]))


while len(q) > 0:
    gridStart, sideRoomsStart, score, previousGrid, oldScore = q.pop()

    hash = ''.join(gridStart[0]) + ''.join(gridStart[1]) + ''.join(gridStart[2])
    if hash in visited and visited[hash] <= score:
        continue

    visited[hash] = score

    goes += 1
    if goes == 11648:
        pass
        goes = 11648

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
                    # print(np.array(grid))
                    sideRooms.remove(homes[pod])
                    if len(sideRooms) == 0:
                        if newScore < bestScore:
                            bestScore = newScore
                        continue
                q.append((grid, sideRooms, newScore, gridStart, score))

    for depth in range(1, 3):
        for i in range(2, 11, 2):
            if i not in sideRoomsStart:
                continue
            pod = gridStart[depth][i]
            if pod != ' ':
                # move to room
                toRoomScore = moveToHomeFromRoom(gridStart, pod, i, depth)
                if toRoomScore > -1:
                    newScore = score + toRoomScore
                    grid = copyGrid(gridStart)
                    grid[depth][i] = ' '
                    homeDone = putPodInHome(grid, pod)
                    sideRooms = sideRoomsStart[:]
                    if homeDone:
                        # print(np.array(grid))
                        sideRooms.remove(homes[pod])
                        if len(sideRooms) == 0:
                            if newScore < bestScore:
                                bestScore = newScore
                                # print(bestScore)
                            continue
                    q.append((grid, sideRooms, newScore, gridStart, score))

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

                    q.append((grid, sideRooms, newScore, gridStart, score))

print(bestScore)
exit()
