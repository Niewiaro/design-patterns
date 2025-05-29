import time


def pairs(seq):
    n = len(seq)
    for i in range(n):
        yield seq[i], seq[(i + 1) % n]


SLOW = 3  # in seconds
LIMIT = 5  # in characters
WARNING = 'too bad, you picked the slow algorithm :('


def all_unique_sort(s):
    if len(s) > LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    srt_str = sorted(s)
    for (c1, c2) in pairs(srt_str):
        if c1 == c2:
            return False
    return True


def all_unique_set(s):
    if len(s) < LIMIT:
        print(WARNING)
        time.sleep(SLOW)
    return True if len(set(s)) == len(s) else False


def all_unique(word, strategy):
    return strategy(word)


def main():
    WORD_IN_DESC = 'Insert word (type quit to exit)> '
    STRAT_IN_DESC = 'Choose strategy: [1] Use a set, [2] Sort and pair> '
    while True:
        word = None
        while not word:
            word = input(WORD_IN_DESC)
            if word == 'quit':
                print('bye')
                return

        if len(word) < LIMIT:
            strategy_picked = all_unique_sort
        else:
            strategy_picked = all_unique_set

        result = all_unique(word, strategy_picked)
        print(f'allUnique({word}): {result}')


if __name__ == '__main__':
    main()
