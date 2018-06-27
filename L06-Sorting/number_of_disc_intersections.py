#!/usr/bin/env python3

import bisect


def solution(A):
    """
    >>> solution([])
    0
    >>> solution([5])
    0
    >>> solution([2, 2])
    1
    >>> solution([1, 5, 2, 1, 4, 0])
    11
    """
    borders = [(c - r, c + r) for c, r in enumerate(A)]
    borders.sort(key=lambda x: (x[0], -x[1]))
    left_radius = tuple(l for l, _ in borders)
    right_radius = tuple(r for _, r in borders)
    count = 0
    for index, r in enumerate(right_radius, 1):
        max_index = bisect.bisect_right(left_radius, r, index)
        count += max_index - index
        if count > 10000000:
            return -1
    return count
