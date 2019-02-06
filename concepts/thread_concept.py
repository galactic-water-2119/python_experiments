from random import random
import threading
import time

progress = 0
result = None
result_available = threading.Event()


def background_calculation():
    # here goes some long calculation
    global progress
    a = 1
    for i in range(100):
        time.sleep(random() * 3)
        progress = i + 1

    # when the calculation is done, the result is stored in a global variable
    for i in range(1,1000):
        a = a * i
        print(a, end="\n")
    global result
    result = 42
    result_available.set()

    # do some more work before exiting the thread
    time.sleep(10)


def main():
    thread = threading.Thread(target=background_calculation)
    thread.start()

    # wait here for the result to be available before continuing
    while not result_available.wait(timeout=5):
        print('\r{}% done...'.format(progress), end='', flush=True)
    print('\r{}% done...'.format(progress))

    print('The result is', result)


if __name__ == '__main__':
    main()