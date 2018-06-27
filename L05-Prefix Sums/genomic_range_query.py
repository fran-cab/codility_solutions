#!/usr/bin/env python3


def solution(S, P, Q):
    """
    >>> solution('CAGCCTA', [2, 5, 0], [4, 5, 6])
    [2, 4, 1]
    """
    response = ['T'] * len(P)
    for i, s in enumerate(S):
        for k, (p, q) in enumerate(zip(P, Q)):
            if p <= i and i <= q and s < response[k]:
                response[k] = s
    impact_factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    return [impact_factor[n] for n in response]


def solution(S, P, Q):
    """
    >>> solution('CAGCCTA', [2, 5, 0, 0, 6], [4, 5, 6, 0, 6])
    [2, 4, 1, 2, 1]
    """
    counters = {
        'A': [0] * len(S),
        'C': [0] * len(S),
        'G': [0] * len(S),
        'T': [0] * len(S)
    }
    for i, s in enumerate(S):
        for count in counters.values():
            count[i] = count[i - 1]
        counters[s][i] += 1
    impact_factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    answers = []
    for p, q in zip(P, Q):
        for k, count in counters.items():
            if count[q] > count[p if p == 0 else p - 1]:
                answers.append(impact_factor[k])
                break
            if p == q:
                answers.append(impact_factor[S[p]])
                break
        else:
            raise Exception('Error inesperado.')
    return answers
