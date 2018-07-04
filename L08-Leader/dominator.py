#!/usr/bin/env python3
from typing import List


def solution(a: List[int]) -> int:
    """
    :param a: A list containing numbers.
    :returns: An index of a number which apears more than half of @a's lenght or -1.
    >>> solution([1, 2])
    -1
    >>> solution([])
    -1
    >>> solution([2, 1, 2, 1, 1])
    4
    """
    if not a:
        return -1
    n = len(a)
    value = -1
    size = 0
    for elem in a:
        if value == elem:
            size =+ 1
        elif size > 0:
            size -= 1
        else:
            value = elem
            size = 1
    count = 0
    index = -1
    for i, elem in enumerate(a):
        if value == elem:
            count += 1
            index = i
    return index if count > n // 2 else -1
