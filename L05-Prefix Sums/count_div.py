#!/usr/bin/env python3


def solution(a: int, b: int, k: int) -> int:
    """
    :return: The number of integers within the range [a..b]
             that are divisible by k.

    >>> solution(6, 11, 2)
    3
    >>> solution(3, 14, 7)
    2
    """
    count = (b - a + 1) // k
    if b % k == 0:
        count += 1
    return count
