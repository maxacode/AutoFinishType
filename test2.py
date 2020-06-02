import test
import time

def test1(): # Test with block=False
    print('test1')

    k = test.KeyGetter()
    try:
        while True:
            if k.kbhit():
                print('Got', repr(k.getch(False)))
                print('Got', repr(k.getch(False)))
            else:
                print('Nothing')

            time.sleep(0.5)
    except KeyboardInterrupt:
        pass
    print(input('Enter something:'))

def test2(): # Test context manager with block=True
    print('test2')

    with KeyGetter() as k:
        try:
            while True:
                if k.kbhit():
                    print('Got', repr(k.getchar(True)))
                    print('Got', repr(k.getchar(True)))
                else:
                    print('Nothing')

                time.sleep(0.5)
        except KeyboardInterrupt:
            pass
    print(input('Enter something:'))

test1()
test2()