#!/usr/bin/env python


def solution(x, y, d):
    """
    >>> solution(1, 1, 1)
    0
    >>> solution(10, 85, 30)
    3
    >>> solution(10, 95, 30)
    3
    >>> solution(10, 105, 30)
    4
    >>> solution(1, 1000000000, 1)
    999999999
    >>> solution(1, 1000000000, 2)
    500000000
    >>> solution(1, 1000000000, 3)
    333333333
    >>> solution(1000000000, 1000000000, 1000000000)
    0

    :param x: initial position
    :param y: final position
    :param d: pase
    :return: The amount of jumps needed to go from @x to @y with a pase of @d
    """
    distance = abs(x - y)
    jumps = distance // d
    if distance % d:
        jumps += 1
    return jumps


if __name__ == '__main__':
    for n in range(1, 1000000001):
        assert solution(n, n, 1) == 0
