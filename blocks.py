
def sum(a, b):
    d = 120
    print('aa=' + str(a))
    print('b=' + str(b))
    a = 100
    return a + b

a = 50
b = 10
c = sum(a, b)
print(c)
d = 0
if a > 40:
    if a > 45:
        print('a>45')
        d = 50
else:
    d = 20
print('d=' + str(d))