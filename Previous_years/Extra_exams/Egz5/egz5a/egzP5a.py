import math

from egzP5atesty import runtests

"""
f(a,b) = minimalana liczba z przedzialu (a,b)
"""


def inwestor(T: list) -> int:
    # tutaj proszę wpisać własną implementację
    n = len(T)

    DP = [[-1 for _ in range(n)] for _ in range(n)]

    def f(a: int, b: int) -> int:
        nonlocal DP, T

        if DP[a][b] != -1:
            return DP[a][b]
        if a == b:
            return T[a]

        DP[a][b] = min(T[b], f(a, b - 1))
        return DP[a][b]

    ans = 0
    for i in range(n):
        for j in range(i + 1, n):
            ans = max(ans, f(i, j) * (j - i + 1))


    return ans


runtests ( inwestor, all_tests=False )

T = [2, 1, 5, 6, 2, 3]
print(inwestor(T))
