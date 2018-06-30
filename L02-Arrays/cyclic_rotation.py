#!/usr/bin/env python3


def solution(a: list, k: int) -> list:
    """
    >>> solution([], 0)
    []
    >>> solution([], 100)
    []
    >>> solution([1] * 100, 100) == [1] * 100
    True
    >>> solution([1, 3], 1)
    [3, 1]
    >>> solution([1, 3], 2)
    [1, 3]

    :param a: An array of integers
    :param k: Number of rotations
    :return: @a rotated @k times
    """
    try:
        n = len(a)
        return a[k % n:] + a[:k % n]
    except ZeroDivisionError:
        return a


if __name__ == '__main__':
    assert solution([], 0) == []
    assert solution([], 1) == []
    array = [1, 2, 2, 1]
    for j in range(100):
        assert solution(array, 1) == solution(array, 1 + j * len(array))
