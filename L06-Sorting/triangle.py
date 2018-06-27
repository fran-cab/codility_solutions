#!/usr/bin/env python3


def solution(A):
    """
    >>> solution([])
    0
    >>> solution([10, 2, 5, 1, 8, 20])
    1
    >>> solution([10, 50, 5, 1])
    0
    """
    if len(A) < 3:
        return 0
    a = sorted(A, reverse=True)
    for i in range(len(A) - 2):
        if a[i] + a[i + 1] > a[i + 2] and \
           a[i] + a[i + 2] > a[i + 1] and \
           a[i + 1] + a[i + 2] > a[i]:
            return 1
    return 0
