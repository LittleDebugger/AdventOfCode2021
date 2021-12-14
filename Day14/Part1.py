import re
from collections import Counter

file = [line.strip() for line in open("input.txt")]
word = file[0]

steps = 10

rules = []

for i in range(2, len(file)):
    s = re.split(' |->', file[i])
    rules.append((s[0], s[3]))

for step in range(steps):
    newWord = ""
    for i in range(len(word) - 1):
        newWord += word[i]
        added = False
        for c in rules:
            if word[i] == c[0][0] and word[i + 1] == c[0][1]:
                added = True
                newWord += c[1]
                continue
        if not added:
            newWord += word[i]
    newWord += word[-1]
    word = newWord

c = Counter(word).most_common()
print(c[0][1] - c[-1][1])
