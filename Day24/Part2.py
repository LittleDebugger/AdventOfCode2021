variables = [
    (1, 14, 12),
    (1, 13, 6),
    (1, 12, 4),
    (1, 14, 5),
    (1, 13, 0),
    (26, -7, 4),
    (26, -13, 15),
    (1, 10, 14),
    (26, -7, 6),
    (1, 11, 14),
    (26, -9, 8),
    (26, -2, 5),
    (26, -9, 14),
    (26, -14, 4)
]

minuses = [5, 6, 8, 10, 11, 12, 13]

queue = [([0], [[0, 0, 0, 0]])]

while len(queue) > 0:
    monad, alus = queue.pop()
    varId = len(monad) - 1
    alu = alus[-1][:]
    alu[0] = monad[-1]  # 1
    alu[1] = alu[3]  # 2 and 3
    alu[1] = (alu[1] % 26)  # 4
    alu[3] //= variables[varId][0]  # 5
    alu[1] += variables[varId][1]  # 6
    alu[1] = 0 if alu[1] == alu[0] else 1  # 7 and 8
    alu[2] = 25  # 9 and 10
    alu[2] *= alu[1]  # 11
    alu[2] += 1  # 12
    alu[3] *= alu[2]  # 13
    alu[2] = alu[0] + variables[varId][2]  # 14 and 15 and 16
    alu[2] *= alu[1]  # 17
    alu[3] += alu[2]  # 18
    if varId in minuses and alu[2] != 0:
        nextMonad = monad[:]
        nextAlu = alus[:]
        while True:
            nextMonad[-1] = nextMonad[-1] + 1
            if nextMonad[-1] == 10:
                nextMonad = nextMonad[:-1]
                nextAlu = nextAlu[:-1]
                continue
            queue.append((nextMonad, nextAlu))
            break
    elif varId == 13:
        print(''.join([str(x) for x in monad]))
        exit()
    else:
        nextMonad = monad[:]
        nextMonad.append(1)
        nextAlu = alus[:]
        nextAlu.append(alu[:])
        queue.append((nextMonad, nextAlu))
