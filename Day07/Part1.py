file = [line.strip() for line in open("input.txt")][0]
crabs = [int(a) for a in file.split(',')]

best = 1000000000000

for target in range(0, max(crabs)):
    total = 0
    for crab in crabs:
        total = total + abs(target - crab)
    if total < best:
        best = total

print(best)
