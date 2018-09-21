from betbright.lru import lru


def fib1(n):
    if n < 2:
        return n
    return fib1(n-1) + fib1(n-2)


@lru()
def fib2(n):
    if n < 2:
        return n
    return fib2(n-1) + fib2(n-2)


if __name__ == '__main__':
    import timeit

    assert fib1(35) == fib2(35)

    without_lru = timeit.timeit(
        'fib1(35)', setup='from __main__ import fib1', number=1)

    with_lru = timeit.timeit(
        'fib2(35)', setup='from __main__ import fib2', number=1)

    print('Fibonacci of 35')
    print(' - Without lru:\t %ss' % without_lru)
    print(' - With lru:\t %ss' % with_lru)
