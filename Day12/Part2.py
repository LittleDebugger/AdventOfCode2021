from collections import defaultdict as dd

file = [line.strip() for line in open("input.txt")]

connections = dd(lambda: [])

for line in file:
    s = line.split('-')
    connections[s[0]].append(s[1])
    connections[s[1]].append(s[0])

t = 0
paths = set()


def go(current, visited, twice):
    global t

    nextVisited = visited[:]

    if current == 'end':
        nextVisited.append(current)
        paths.add(', '.join(nextVisited))
        return

    if current == twice:
        if current.upper() in nextVisited:
            return
        elif current in nextVisited:
            nextVisited.append(current.upper())
        else:
            nextVisited.append(current)
    else:
        nextVisited.append(current)

    for next in connections[current]:
        if next != twice and next.islower() and next in visited:
            continue

        go(next, nextVisited, twice)


for twice in connections:
    if twice != 'start' and twice != 'end' and twice.islower():
        go('start', [], twice)

print(len(paths))
