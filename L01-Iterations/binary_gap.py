#!/usr/bin/env python3


def solution(n: int) -> int:
    """
    >>> solution(1041)
    5
    >>> solution(20)
    1
    >>> solution(15)
    0
    >>> solution(9)
    2
    >>> solution(0x81)
    6
    >>> solution(0x404010F1)
    9

    :param n: A positive integer number
    :return: n's binary gap or zero if n doesn't have one
    """
    binary_gap = 0
    count = 0
    # skip the lowest zeros
    while n and (n & 1) == 0:
        n = n >> 1
    while n:
        while n & 1:
            n = n >> 1
        while n and (n & 1) == 0:
            count += 1
            n = n >> 1
        if n & 1 and binary_gap < count:
            binary_gap = count
        count = 0
    return binary_gap


if __name__ == '__main__':
    assert solution(1) == 0
    assert solution(2) == 0
    assert solution(1041) == 5
    assert solution(20) == 1
    assert solution(15) == 0
    assert solution(9) == 2

    assert solution(2147483647) == solution(0b11111111111111111111111111111111)
    assert solution(2147483647) == solution(0xffffffff)

    print(solution(129))
    print(solution(130))
    print(solution(132))
