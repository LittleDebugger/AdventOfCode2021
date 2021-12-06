from collections import defaultdict as dd

file = [line.strip() for line in open("input.txt")][0]
ages = [int(a) for a in file.split(',')]

ageCount = dd(lambda: 0)

for age in ages:
    ageCount[age] = ageCount[age] + 1

for age in range(0, 256):
    nextAgeCount = dd(lambda: 0)

    for b in range(0, 8):
        nextAgeCount[b] = ageCount[b + 1]

    nextAgeCount[8] = ageCount[0]
    nextAgeCount[6] = nextAgeCount[6] + ageCount[0]
    ageCount = nextAgeCount

total = 0
for age in ageCount:
    total += ageCount[age]
print(total)
