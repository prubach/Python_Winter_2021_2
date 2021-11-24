# rows = 5
# sum ? how many x's
#
#     x x x x x
#      x x x x
#       x x x
#        x x
#         x

n = int(input("Enter number "))
sum = 0
# loop from 1 to n
for num in range(1, n + 1, 1):
    sum = sum + num
print("Sum of first ", n, "numbers is: ", sum)

sum_num = (n * (n + 1)) / 2
print('Sum as sequence: {}'.format(sum_num))

