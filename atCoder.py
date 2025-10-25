a = int(input())

total = 1
m = 998244353
l = dict()


def go(v):
    global m, l
    if v in l:
        return l[v]

    if v > 4:
        r = (((go(v // 2)) % m) * ((go(v // 2 + (v % 2))) % m)) % m
        l[v] = r
        return r
    else:
        l[v] = v
        return v

print(go(a))
