if __name__ == '__main__':
    a = 10
    b = -2352759375923759023758923475923576923576923769123476892376923768923769072369723692376890723
    c = a + b
    print(type(c))
    #print('c:' + str(c))
    print('c:{}'.format(c))

    af = 242.033
    bf = 6596725972395734957234572389572395712572389751289575.352
    cf = af + bf
    print(type(cf))
    print('cf:{}'.format(cf))

    print(1.79e+308)
    print(1.8e+308)

    bb = 0b11111111
    print(bb)

    bx = 0xff
    print(bx)

    print(bb/bx)

    f = 5

    print(f**3)
    g = 12
    print('div g: {}'.format(g % 5))

    h = 'ff'
    print(int(h, 16))
    h1 = '563463'
    h1i = int(h1)
    print(h1.isdigit())
    print(h1.isalpha())
    print(h1.isalnum())

    print(type(h1))
    print(type(h1i))

    fa = 100
    print(type(fa))
    fa = 100.3563
    print(type(fa))
    print(round(fa, 2))
