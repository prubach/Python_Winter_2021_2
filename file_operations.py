f = 'main.py'
with open(f, 'r') as file_in:
    lines = file_in.readlines()
    i = 0
    for line in lines:
        print('{}: {}'.format(i, line))
        i += 1
