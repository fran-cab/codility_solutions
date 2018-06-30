#!/usr/bin/env python3
from collections import deque


def solution(s: str) -> int:
    """
    >>> solution('{[()()]}')
    1
    >>> solution('([)()]')
    0
    """
    m = {'{': '}', '[': ']', '(': ')'}
    stack = deque()
    for token in s:
        if token in '{[(':
            stack.append(token)
        elif m[stack.pop()] != token:
            return 0
    return 0 if stack else 1
