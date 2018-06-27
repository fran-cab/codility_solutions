#!/usr/bin/env python3
from collections import deque


def solution(S):
    """
    >>> solution('{[()()]}')
    1
    >>> solution('([)()]')
    0
    """
    m = {'{': '}', '[': ']', '(': ')'}
    stack = deque()
    for s in S:
        if s in '{[(':
            stack.append(s)
        elif m[stack.pop()] != s:
            return 0
    return 0 if stack else 1
