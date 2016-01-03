i = 0

def test():
    global i
    print i

def test1():
    global i
    i += 1
    print i

if __name__ == '__main__':
    test()
    test1()
    test()
