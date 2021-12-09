from collections import Counter

file = [[int(c) for c in line.strip()] for line in open("input.txt")]

visited = set()
location_basins = dict()
basinIx = 0


def check_location(x, y):
    loc = (x, y)
    if loc in visited:
        return
    if x < 0 or y < 0 or x >= len(file[0]) or y >= len(file):
        return

    if file[y][x] == 9:
        return

    visited.add(loc)
    location_basins[loc] = basinIx

    if file[y][x] < 9:
        check_location(x + 1, y)
        check_location(x - 1, y)
        check_location(x, y + 1)
        check_location(x, y - 1)


for yy in range(len(file)):
    for xx in range(len(file[0])):
        if (xx, yy) not in visited:
            check_location(xx, yy)
            basinIx = basinIx + 1

basin_sizes = Counter(list(location_basins.values())).most_common()

print(basin_sizes[0][1] * basin_sizes[1][1] * basin_sizes[2][1])
