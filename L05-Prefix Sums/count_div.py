#!/usr/bin/env python3


def solution(A, B, K):
    """
    :return: The number of integers within the range [A..B] 
             that are divisible by K.

    >>> solution(6, 11, 2)
    3
    >>> solution(3, 14, 7)
    2
    """
    count = (B - A + 1) // K
    if B % K == 0:
        count += 1
    return count
