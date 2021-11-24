l2d = [[4, 7, 8],
       [6, 4, 8],
       [3, 5, 8],
       [2, 7, 8]]
print(l2d[2][0])
# TODO
# sum rows
# sum cols
# sum all elements
sums = []
for el in l2d:
    sums.append(sum(el))
print(sums)

print('sum all based on sum rows: {}'.format(sum(sums)))


#sums_cols = [0, 0, 0]
sums_cols = []
#sums_cols = [0, 0, 0]
for el in l2d:
    for i in range(len(el)):
        if len(sums_cols) > i:
            sums_cols[i] += el[i]
        else:
            sums_cols.append(el[i])
print(sums_cols)

print('sum all based on sum cols: {}'.format(sum(sums)))

#sums2 = [sum(el) for el in l2d if len(el) > 2]
#sums2 = [sum(el) for el in l2d]
#print(sums2)

import numpy as np

print(np.sum(l2d, axis=0))
print(np.sum(l2d, axis=1))
print(np.sum(l2d))
