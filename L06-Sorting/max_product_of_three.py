#!/usr/bin/env python3


def solution(a: list) -> int:
    """
    >>> solution([-3, 1, 2, -2, 5, 6])
    60
    >>> solution([6, 5, 4])
    120
    """
    a.sort()
    return max(a[0] * a[1] * a[-1], a[-3] * a[-2] * a[-1])
