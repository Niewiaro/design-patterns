import functools


def memoize(fn):
    cache = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]

    return memoizer


def memoize_debug(fn):
    cache = dict()

    @functools.wraps(fn)
    def memoizer(*args):
        if args not in cache:
            cache[args] = fn(*args)
            print([*cache.items()][-1])
        return cache[args]

    return memoizer


def conditional_decorator(condition, real_decorator):
    def wrapper(func):
        if condition:
            return real_decorator(func)
        return func

    return wrapper


def memoize_with_debug_option(debug: bool = False):
    def wrapper(func):
        if debug:
            return memoize_debug(func)
        return memoize(func)

    return wrapper


def benchmark(func):
    """
    A decorator that prints the time a function takes
    to execute.
    """
    import time
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        res = func(*args, **kwargs)
        print("{0} {1:.6f}s".format(func.__name__, time.perf_counter() - t))
        return res

    return wrapper


def logging(func):
    """
    A decorator that logs the activity of the script.
    (it actually just prints it, but it could be logging!)
    """

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print("{0} {1} {2}".format(func.__name__, args, kwargs))
        return res

    return wrapper


def counter(func):
    """
    A decorator that counts and prints the number of times a function has been executed
    """

    def wrapper(*args, **kwargs):
        wrapper.count = wrapper.count + 1
        res = func(*args, **kwargs)
        print("{0} has been used: {1}x".format(func.__name__, wrapper.count))
        return res

    wrapper.count = 0
    return wrapper
