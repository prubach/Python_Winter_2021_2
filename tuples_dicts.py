t1 = (5, 8, 8)
print(t1[2])

d1 = {0 : 525, 1: 6747, 2: 3747}
print(d1[0])

d1 = {'a': 525, 'a': 56464, 'bb': 56464, 'ccc': 3747}
d1['ddd'] = 436536
print(d1)
print(d1['a'])

for k, v in d1.items():
    print('{}: {}'.format(k, v))


for k in d1.keys():
    print('{}: {}'.format(k, d1[k]))



