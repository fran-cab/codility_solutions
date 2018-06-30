#!/usr/bin/env python3


def solution(a: list) -> int:
    """
    >>> solution([2, 1, 1, 2, 3, 1])
    3
    >>> solution([])
    0
    >>> solution([1, 2, 3, 4]) == solution([4, 3, 2, 1])
    True
    >>> solution([1])
    1
    """
    if not a:
        return 0
    a_sorted = sorted(a)
    count = 1
    for i in range(1, len(a_sorted)):
        if a_sorted[i] != a_sorted[i-1]:
            count += 1
    return count
