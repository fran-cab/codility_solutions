#!/usr/bin/env python3
from typing import List


def find_leader_candidate(a: List[int]) -> int:
    """
    :param a: A list containing numbers.
    :returns: An index of a number which apears more than half of @a's lenght or -1.
    """
    if not a:
        return -1
    n = len(a)
    value = -1
    size = 0
    for elem in a:
        if value == elem:
            size =+ 1
        elif size > 0:
            size -= 1
        else:
            value = elem
            size += 1
    return value


def solution(a: List[int]) -> int:
    """
    :param a: A non empty list of numbers.
    :returns: The number of equi leaders.

    >>> solution([1])
    0
    >>> solution([1, 2, 1, 1])
    2
    """
    candidate = find_leader_candidate(a)
    total = 0
    acum = []
    for i in a:
        if candidate == i:
            total += 1
        acum.append(total)
    n = len(a)
    equi_leaders = 0
    if total > n // 2:
        # candidate is in fact a leader
        for size, count in enumerate(acum, 1):
            if count > size // 2 and total - count > (n - size) // 2:
                equi_leaders += 1
    return equi_leaders
