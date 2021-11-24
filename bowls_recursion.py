
def sum_bowls_recursion(r):
    if r==1:
        return 1
    else:
        return r + sum_bowls_recursion(r-1)

n = int(input("Enter number "))
print('Sum bowls using recursion: {}'.format(sum_bowls_recursion(n)))