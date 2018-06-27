#!/usr/bin/env python


def solution(a):
    """
    >>> solution([1, 3])
    2
    """
    counter = [0] * (len(a) + 1)
    for x in a:
        counter[x-1] += 1
    for x, count in enumerate(counter, 1):
        if not count:
            return x


if __name__ == '__main__':
    for n in range(10):
        a = [i for i in range(1, n + 2)]
        for i in range(len(a)):
            assert solution(a[:i] + a[i + 1:]) == i + 1
