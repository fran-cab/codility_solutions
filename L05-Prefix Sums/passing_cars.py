#!/usr/bin/env python3


def solution(a: list) -> int:
    """
    :return: The number of pairs of passing cars

    >>> solution([0])
    0
    >>> solution([1, 0])
    0
    >>> solution([0, 1])
    1
    >>> solution([0, 1, 0, 1, 1])
    5
    """
    count = 0
    step = 0
    for num in a:
        count = count + step * num
        step = step + 1 - num
    return count
