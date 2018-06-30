#!/usr/bin/env python3


def solution(s: str) -> int:
    """
    >>> solution('(()(())())')
    1
    >>> solution('())')
    0
    """
    count = 0
    m = {'(': 1, ')': -1}
    for token in s:
        count += m[token]
        if count < 0:
            return 0
    return 0 if count else 1
