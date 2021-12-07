file = [line.strip() for line in open("input.txt")][0]
crabs = [int(a) for a in file.split(',')]

best = 1000000000000

for target in range(0, max(crabs)):
    total = 0
    for crab in crabs:
        total = total + int((abs(target - crab) + 1) * (abs(target - crab) / 2))
    if total < best:
        best = total

print(best)
