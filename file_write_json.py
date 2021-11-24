import json
d1 = {'a': 525, 'a': 56464, 'bb': 56464, 'ccc': 3747, 'ddd': [25356, 474, 6346, 'wwhwrh']}
#d1['ddd'] = 436536

with open('data/out_d.json', 'w') as f:
    json.dump(d1, f)


with open('data/out_d.json', 'r') as f:
    out_d = json.load(f)
    print(out_d)
    print(type(out_d))