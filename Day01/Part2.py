file = [int(line.strip()) for line in open("input.txt")]

t = 0
for x in range(0, len(file) - 3):
    if file[x] + file[x + 1] + file[x + 2] < file[x + 1] + file[x + 2] + file[x + 3]:
        t += 1

print(t)
