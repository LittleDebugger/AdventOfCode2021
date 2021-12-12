from collections import defaultdict as dd

file = [line.strip() for line in open("input.txt")]

connections = dd(lambda: [])

for line in file:
    s = line.split('-')
    connections[s[0]].append(s[1])
    connections[s[1]].append(s[0])

t = 0


def go(current, visited):
    global t
    if current == 'end':
        t += 1
        return

    nextVisited = visited[:]
    if current[0].islower():
        nextVisited.append(current)

    for next in connections[current]:
        if next in visited:
            continue
        go(next, nextVisited)


go('start', [])

print(t)
