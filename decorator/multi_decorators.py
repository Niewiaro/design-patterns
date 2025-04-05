from my_math.decorators import memoize, memoize_debug, memoize_with_debug_option, counter, logging, benchmark, conditional_decorator

BENCHMARK = False

# @memoize
# def number_sum(n):
#     from number_sum import number_sum
#     number_sum(n)

# NOTE: this decorator wraps only one execution. Recursive calls do not have decorator
# from number_sum import number_sum
# number_sum = memoize_debug(number_sum)

@memoize_debug
@conditional_decorator(BENCHMARK, benchmark)
def number_sum(n):
    """Returns the sum of the first n numbers"""
    assert (n >= 0), 'n must be >= 0'
    if n == 0:
        return 0

    return n + number_sum(n - 1)

# @memoize
# @memoize_debug
@memoize_with_debug_option(True)
def fibonacci(n):
    """Returns the suite of Fibonacci numbers"""
    assert (n >= 0), 'n must be >= 0'
    if n in (0, 1):
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


@counter
@benchmark
@logging
def reverse_string(string):
    return string[::-1]


def main() -> None:
    from timeit import Timer
    to_execute = [(number_sum, Timer('number_sum(300)', 'from __main__ import number_sum')),
                  (fibonacci, Timer('fibonacci(100)', 'from __main__ import fibonacci'))]

    for item in to_execute:
        fn = item[0]
        print(f'Function "{fn.__name__}": {fn.__doc__}')
        t = item[1]
        print(f'Time: {t.timeit()}')
        print()

    print(reverse_string("Able was I ere I saw Elba"))
    print()
    print(reverse_string(
        "A man, a plan, a canoe, pasta, heros, rajahs, a coloratura, maps, snipe, percale, macaroni, a gag, a banana bag, a tan, a tag, a banana bag again (or a camel), a crepe, pins, Spam, a rut, a Rolo, cash, a jar, sore hats, a peon, a canal: Panama!"))


if __name__ == "__main__":
    main()
