file = [int(line.strip()) for line in open("input.txt")]

t = 0
for x in range(1, len(file)):
    if file[x] > file[x - 1]:
        t += 1

print(t)
