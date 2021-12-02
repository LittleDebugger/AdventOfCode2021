file = [line.strip() for line in open("input.txt")]

x = 0
y = 0
aim = 0

d = dict()
d['forward'] = (1, 0)
d['down'] = (0, 1)
d['up'] = (0, -1)

for line in file:
    s = line.split(' ')
    x += (d[s[0]][0] * int(s[1]))
    aim += (d[s[0]][1] * int(s[1]))

    if s[0] == 'forward':
        y += int(s[1]) * aim


print(x*y)
