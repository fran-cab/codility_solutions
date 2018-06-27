#!/usr/bin/env python3
from collections import deque


def solution(A, B):
    """
    >>> solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])
    2
    """
    u_fishes = deque()
    d_count = 0
    for size, dir in zip(A, B):
        if dir == 1:
            u_fishes.append(size)
        else:
            while u_fishes:
                if u_fishes[-1] < size:
                    u_fishes.pop()
                elif u_fishes[-1] == size:
                    u_fishes.pop()
                    break
                else:
                    break
            if not u_fishes:
                d_count += 1
    return len(u_fishes) + d_count
