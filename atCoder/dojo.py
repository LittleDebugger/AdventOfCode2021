import numpy as np

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(np.array(a))

# newA = []
# for i in range(len(a)):
#   l = []
#  newA.append(l)
# for j in range(len(a[0])):
#    l.append(a[len(a) - j - 1][i])

# print(np.array(newA))
# newB = [[a[len(a) - j - 1][i] for j in range(len(a[0]))] for i in range(len(a))]
# print (np.array(newB))


[l.reverse() for l in a]


print(np.array(a))
