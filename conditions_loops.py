p = True
q = True

if p and not q:
    print("p and q = TRUE")
else:
    print("p and q = NOT TRUE")

if p or q:
    print("p or q = TRUE")
else:
    print("p or q = NOT TRUE")

# xor
if p ^ q:
    print("p or q = TRUE")
else:
    print("p or q = NOT TRUE")


for i in range(2, 8):
    if i==3:
        continue
    print(i)
    if i==5:
        break


def sum(a, b):
    return a + b

print(sum(56,3))