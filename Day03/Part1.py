from collections import Counter

file = [line.strip() for line in open("input.txt")]

oxygen = ''
scrubber = ''

for x in range(0, len(file[0])):
    oxygenDigit = Counter([a[x] for a in file]).most_common()[0][0]
    scrubberDigit = Counter([a[x] for a in file]).most_common()[-1][0]

    oxygen += oxygenDigit
    scrubber += scrubberDigit

print(int(oxygen, 2) * int(scrubber, 2))


