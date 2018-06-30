#!/usr/bin/env python3


def solution(a: list) -> int:
    """
    >>> solution([1, 4, 1])
    0
    >>> solution([-1, -2, -3, -2])
    1
    >>> solution([4, 2, 2, 5, 1, 5, 8])
    1
    """
    start = 0
    min_ = 10001
    for i in range(len(a) - 1):
        avg = (a[i] + a[i + 1]) / 2
        if min_ > avg:
            min_, start = avg, i
        try:
            avg = (a[i] + a[i + 1] + a[i + 2]) / 3
            if min_ > avg:
                min_, start = avg, i
        except IndexError:
            pass
    return start
