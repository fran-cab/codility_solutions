#!/usr/bin/env python3
from collections import deque


def solution(a: list, b: list) -> int:
    """
    >>> solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])
    2
    """
    u_fishes = deque()
    d_count = 0
    for size, dir_ in zip(a, b):
        if dir_ == 1:
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
