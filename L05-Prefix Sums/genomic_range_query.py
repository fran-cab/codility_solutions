#!/usr/bin/env python3


def solution(s: str, p: list, q: list) -> list:
    """
    >>> solution('CAGCCTA', [2, 5, 0], [4, 5, 6])
    [2, 4, 1]
    """
    response = ['T'] * len(p)
    for i, s in enumerate(s):
        for k, (p, q) in enumerate(zip(p, q)):
            if p <= i <= q and s < response[k]:
                response[k] = s
    impact_factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    return [impact_factor[n] for n in response]


def solution(s: str, p: list, q: list) -> list:
    """
    >>> solution('CAGCCTA', [2, 5, 0, 0, 6], [4, 5, 6, 0, 6])
    [2, 4, 1, 2, 1]
    """
    counters = {
        'A': [0] * len(s),
        'C': [0] * len(s),
        'G': [0] * len(s),
        'T': [0] * len(s)
    }
    for i, s in enumerate(s):
        for count in counters.values():
            count[i] = count[i - 1]
        counters[s][i] += 1
    impact_factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    answers = []
    for p, q in zip(p, q):
        for k, count in counters.items():
            if count[q] > count[p if p == 0 else p - 1]:
                answers.append(impact_factor[k])
                break
            if p == q:
                answers.append(impact_factor[s[p]])
                break
        else:
            raise Exception('Unexpected error')
    return answers
