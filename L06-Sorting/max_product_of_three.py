#!/usr/bin/env python3


def solution(A):
    """
    >>> solution([-3, 1, 2, -2, 5, 6])
    60
    >>> solution([6, 5, 4])
    120
    """
    A.sort()
    return max(A[0] * A[1] * A[-1], A[-3] * A[-2] * A[-1])
