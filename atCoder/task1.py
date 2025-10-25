n = int(input())

modu = 998244353


previous = [1 for _ in range(0, 11)]
current = [1 for _ in range(0, 11)]

previous[0] = 0
current[0] = 0
previous[10] = 0
current[10] = 0


for ii in range(2, n + 1):
    aro = current
    current = previous
    previous = aro
    for i in range(1, 10):
        current[i] = ((previous[i - 1] % modu) + (previous[i] % modu) + (previous[i + 1] % modu)) % modu

print(sum([c for c in current]) % 998244353)
