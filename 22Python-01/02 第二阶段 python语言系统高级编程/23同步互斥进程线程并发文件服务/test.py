"""
    GIL测试
"""


def count(x, y):
    c = 0
    while c < 7000000:
        x += 1
        y += 1
        c += 1


def io():
    write()
    read()


def write():
    f = open('test.txt','w')
    for i in range(1800000):
        f.write("hello word\n")
    f.close()


def read():
    f = open('test.txt')
    f.readline()
    f.close()
