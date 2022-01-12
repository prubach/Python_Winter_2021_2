import sys

#print('Hello')
#a = None
#a.abv = 3525
#sys.stdout.write('OK')
#sys.stderr.write('Error')
#sys.exit(1)

class MyError(Exception):
    pass

try:
    a = int(input('Provide a: '))
    b = 15
    c = b / a
    print('c: {}'.format(c))
    if c > 10:
        raise MyError('c is greater than 10')
except ZeroDivisionError as de:
    print('I got zero division: {}'.format(de))
except ArithmeticError as de:
    print('I got arithmetic error: {}'.format(de))
except MyError as me:
    print('MyError: {}'.format(me))
# except Exception as e:
#     print(type(e))
#     print('Got Exception: {}'.format(e))

print('Finalizing my script')