#!/usr/bin/env python3


def solution(n: int, a: list) -> list:
    """
    >>> solution(5, [3, 4, 4, 6, 1, 4, 4])
    [3, 2, 2, 4, 2]
    """
    counters = [0] * n
    max_counter = n + 1
    cur_max = 0
    for num in a:
        if num == max_counter:
            counters = [cur_max] * n
        else:
            counters[num - 1] += 1
            if counters[num - 1] > cur_max:
                cur_max += 1
    return counters
