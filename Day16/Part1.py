file = [line.strip() for line in open("input.txt")]

line = file[0]

st = ''

for c in line:
    n = bin(int(c, 16))[2:]
    while len(n) < 4:
        n = '0' + n
    st += n

t = 0
s = st

big = 10000000

def go(p, packets, s):
    global t
    print('****************************************')

    i = 0
    while i < packets and p < len(s) - 7:
        i += 1
        version = int(s[p:p + 3], 2)
        t += version

        type = int(s[p + 3: p + 6], 2)

        if type == 4:
            p += 6
            while True:
                if s[p] != '1':
                    break
                p += 5
            p += 5
        else:
            if s[p + 6] == '0': # is 0, then the next 15 bits are a number that represents the total length in bits
                print('15 bits')
                p += 7
                length = s[p:p + 15]
                ac = int(length, 2)
                print('length = ', ac)
                p += 15

                go(p, big, s)
                p += ac

            else: # 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
                print('11 bits')
                p += 7
                packets = int(s[p:p + 11], 2)
                p += 11
                p = go(p, packets, s)

    return p


go(0, big, s)

print(t)
