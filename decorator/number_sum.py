from my_math.decorators import memoize


def number_sum(n):
    """Returns the sum of the first n numbers"""
    assert (n >= 0), 'n must be >= 0'
    if n == 0:
        return 0

    return n + number_sum(n - 1)


sum_cache = {0: 0}


def number_sum_cache(n):
    """Returns the sum of the first n numbers"""
    assert (n >= 0), 'n must be >= 0'
    if n in sum_cache:
        return sum_cache[n]
    res = n + number_sum(n - 1)
    # Add the value to the cache
    sum_cache[n] = res
    return res


@memoize
def number_sum_memoize(n):
    """Returns the sum of the first n numbers"""
    assert (n >= 0), 'n must be >= 0'
    if n in sum_cache:
        return sum_cache[n]
    res = n + number_sum(n - 1)
    # Add the value to the cache
    sum_cache[n] = res
    return res


def number_sum_fsum(n):
    import math
    return math.fsum([x for x in range(1, n + 1)])


def main() -> None:
    from timeit import Timer
    number = 100

    functions = ['number_sum', 'number_sum_cache', 'number_sum_memoize', 'number_sum_fsum']

    for f in functions:
        t = Timer(f'{f}({number})', f'from __main__ import {f}')
        print(f'Time of {f}: ', t.timeit())


if __name__ == '__main__':
    main()
