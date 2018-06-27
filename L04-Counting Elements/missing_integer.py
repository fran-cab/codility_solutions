#!/usr/bin/env python3
from collections import Counter

def solution(A):
    """
    Given an array A of N integers, returns the smallest positive
    integer (greater than 0) that does not occur in A.

    :param A: An array of N integers
    :return: The smallest positive (lesser than N + 2]) that does not occur in A.

    >>> solution([0])
    1
    >>> solution([1])
    2
    >>> solution([1, 2, 3])
    4
    >>> solution([-1,-2,-3])
    1
    >>> solution([2, 3, 4]) == solution([4, 3, 2])
    True
    """
    counter = Counter(A)
    for n in range(1, len(A) + 2):
        if n not in counter:
            return n
