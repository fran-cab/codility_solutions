#!/usr/bin/env python3
import numpy as np
import array


def solution(A):
    """
    >>> solution([1,2,3,4])
    1

    :param A:
    :return:
    """
    a_size = len(A)
    counter = np.zeros(a_size + 1)
    for num in A:
        try:
            counter[num] += 1
        except IndexError:
            return 0
        if counter[num] > 1:
            return 0
    return 1


def test():
    test_array = []
    for num in range(1, 1001):
        test_array.append(num)
        assert solution(test_array) == 1


if __name__ == '__main__':
    test()
