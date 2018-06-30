#!/usr/bin/env python3


def solution(x: int, a: list) -> int:
    """
    Finds the earliest time at which a frog can cross a river.

    :param x: Number of positions a leaf can fall.
    :param a: A list of positions.
    :returns: The time which a frog can get from position 0 to position X+1
              or -1 if it can never reach it.

    >>> solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
    6
    """
    positions = set(range(1, x + 1))
    for time, position in enumerate(a):
        positions.discard(position)
        if not positions:
            return time
    else:
        return -1
