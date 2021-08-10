from file_two import *


@decorator
def test():
    n = 1
    lst = []
    number = 32451341
    while n-1 < number:
        n += 2
        if number % n == 0:
            lst.append(n)
    print(lst)


test()