import _pickle
d1 = {'a': 525, 'a': 56464, 'bb': 56464, 'ccc': 3747}
d1['ddd'] = 436536

with open('data/out_d.dat', 'wb') as f:
    _pickle.dump(d1, f)


with open('data/out_d.dat', 'rb') as f:
    out_d = _pickle.load(f)
    print(out_d)
    print(type(out_d))