from collections import Counter

file = [line.strip() for line in open("input.txt")]

oxygen = ''
scrubber = ''

answerO = ''
answerS = ''

current = file[:]

for x in range(0, len(file[0])):
    digit = Counter([a[x] for a in current]).most_common()

    oxygenNext = digit[0][0]

    if digit[0][1] == digit[1][1]:
        oxygenNext = '1'

    oxygen += oxygenNext

    filtered = list(filter(lambda x: x.startswith(oxygen), current))
    current = filtered

    if len(filtered) == 1:
        answerO = filtered[0]
        break

current = file[:]

# duplicating this was a bad idea...

for x in range(0, len(file[0])):
    b = Counter([a[x] for a in current]).most_common()

    bNext = b[-1][0]

    if b[-1][1] == b[-2][1]:
        bNext = '0'

    scrubber += bNext

    filtered = list(filter(lambda x: x.startswith(scrubber), current))
    current = filtered

    if len(filtered) == 1:
        answerS = filtered[0]
        break

print(int(answerO, 2) * int(answerS, 2))



