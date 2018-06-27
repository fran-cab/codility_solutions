#!/usr/bin/env python3


def solution(N, A):
    """
    >>> solution(5, [3, 4, 4, 6, 1, 4, 4])
    [3, 2, 2, 4, 2]
    """
    counters = [0] * N
    max_counter = N + 1
    cur_max = 0
    for num in A:
        if num == max_counter:
            counters = [cur_max] * N
        else:
            counters[num - 1] += 1
            if counters[num - 1] > cur_max:
                cur_max += 1
    return counters
