import time


def decorator(func):
    def wrap(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(round(time.time() - start, 3), 'This time to finish function')
        print('no ok')
    return wrap