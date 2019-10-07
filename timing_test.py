from timeit import timeit as t


def test():
    x = 0
    x = x+1

def test2():
    x = 0
    x += 1

if __name__ == '__main__':
    print(t("test", setup="from __main__ import test", number=1000000))
    print(t("test2()", setup="from __main__ import test2", number=1000000))