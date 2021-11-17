import sys

if __name__ == '__main__':
    print('Input args:')
    print(sys.argv)
    for el in sys.argv:
        print('{}: {}'.format(type(el), el))