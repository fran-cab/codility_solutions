#!/usr/bin/env python3


def solution(A):
    """
    >>> solution([1, 4, 1])
    0
    >>> solution([-1, -2, -3, -2])
    1
    >>> solution([4, 2, 2, 5, 1, 5, 8])
    1
    """
    start = 0
    min = 10001
    for i in range(len(A)-1):
       avg = (A[i] + A[i + 1]) / 2
       if min > avg:
           min, start = avg, i
       try:
           avg = (A[i] + A[i + 1] + A[i + 2]) / 3
           if min > avg:
               min, start = avg, i
       except IndexError:
           pass
    return start
