import re
from collections import defaultdict as dd
from collections import Counter

file = [line.strip() for line in open("input.txt")]
word = list(file[0])

start = word[0]
end = word[-1]

steps = 40

pairs = dd(lambda: 0)
for i in range(len(word) - 1):
    pairs[word[i] + word[i + 1]] += 1

rules = dict()

for i in range(2, len(file)):
    s = re.split(' |->', file[i])
    rules[s[0][0] + s[0][1]] = s[3]


for i in range(0, steps):
    newPairs = dd(lambda: 0)
    for p in pairs:
        newPairs[p] = pairs[p]
    added = False
    for c in rules:
        if c in pairs and pairs[c] > 0:
            added = True
            newPairs[c[0] + rules[c]] += pairs[c]
            newPairs[rules[c] + c[1]] += pairs[c]
            newPairs[c] -= pairs[c]
    pairs = newPairs

full = dd(lambda: 0)
for p in pairs:
    full[p[0]] += pairs[p]
    full[p[1]] += pairs[p]

for f in full:
    full[f] //= 2

full[start] += 1
full[end] += 1

c = Counter(full).most_common()
print(c[0][1] - c[-1][1])
