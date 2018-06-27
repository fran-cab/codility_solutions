#!/usr/bin/env python3


def solution(S: str) -> int:
    """
    >>> solution('(()(())())')
    1
    >>> solution('())')
    0
    """
    count = 0
    m = {'(': 1, ')': -1}
    for s in S:
        count += m[s]
        if count < 0:
            return 0
    return 0 if count else 1
