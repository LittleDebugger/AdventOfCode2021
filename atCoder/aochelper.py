ss = input()
q = int(input())

l = dict()
l['A'] = 'BC'
l['B'] = 'CA'
l['C'] = 'AB'

inps = []


for i in range(q):
    inps.append([int(x) for x in input().split()])

for t, k in inps:
    k = k - 1
    #print(t, k)
    num = 2 ** t
    #print('num = ',num)
    s = ss
    letter = ''
    for _ in range(t + 1):
        letter = s[(k // num)]
     #   print(k, num, k // num, s, letter)

        s = l[letter]
        k =  k % num
        num = num // 2
    print(letter)

