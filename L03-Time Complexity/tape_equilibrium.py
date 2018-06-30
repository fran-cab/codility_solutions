#!/usr/bin/env python3


def solution(a: list) -> int:
    """
    >>> solution([3, 1, 2, 4, 3])
    1
    """
    return min(abs(sum(a[:i]) - sum(a[i:])) for i in range(len(a)))


def solution(a: list) -> int:
    """
    >>> solution([3, 1, 2, 4, 3])
    1
    """
    sums = [0] * len(a)
    acum = 0
    for i, x in enumerate(a):
        acum += x
        sums[i] = acum
    return min(abs(acum - 2 * s) for s in sums[:-1])


if __name__ == '__main__':
    assert solution([3, 1, 2, 4, 3]) == 1
