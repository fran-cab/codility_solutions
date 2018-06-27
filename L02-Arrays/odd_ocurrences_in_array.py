#!/usr/bin/env python
from collections import Counter


def solution(a):
    """
    >>> solution([1,2,3] * 14 + [4])
    4
    >>> solution([3, 3, 3, 4, 4])
    3

    :param a:
    :return:
    """
    c = Counter(a)
    return next(k for k, v in c.iteritems() if v % 2)


if __name__ == '__main__':
    assert solution([1, 2, 3] * 14 + [4]) == 4
    assert solution([4] + [1, 2, 3] * 14) == 4

    for i in range(20):
        assert solution([i]) == i
