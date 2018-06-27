#!/usr/bin/env python3
from collections import deque


def solution(H):
    """
    >>> solution([3])
    1
    >>> solution([8, 8, 5, 7, 9, 8, 7, 4, 8])
    7
    """
    stones = 0
    stack = deque([0])
    for h in H:
        while stack[-1] > h:
            stack.pop()
        if stack[-1] < h:
            stack.append(h)
            stones += 1
    return stones
