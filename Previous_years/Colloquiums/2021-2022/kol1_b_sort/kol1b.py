from kol1btesty import runtests
from typing import List

"""
Find anagrams. Alorthim starta from changing words to arrays with counter of type of letter. 
This arrays are sorted by radix && counting sort by all 26 letter. Than loop looks for most common word in this sorted 
arrays.
"""


def countingsort(A: List[List[int]], k: int, index: int) -> None:  # stabliny count po kazdym indexie
    n = len(A)
    C = [0 for _ in range(k)]
    B = [0 for _ in range(n)]

    for i in range(n):
        C[A[i][index]] += 1

    for i in range(1, k):
        C[i] = C[i] + C[i - 1]

    for i in range(n - 1, -1, -1):
        B[C[A[i][index]] - 1] = A[i]
        C[A[i][index]] -= 1

    for i in range(n):
        A[i] = B[i]


def f(T: List[str]) -> int:
    n = len(T)
    A = [[0 for _ in range(26)] for _ in range(n)]

    for i in range(n):
        for s in T[i]:
            A[i][ord(s) - 97] += 1

    for i in range(26):
        k = 0
        for j in range(n):
            k = max(A[j][i], k)  # finding k for counting sort

        k += 1
        countingsort(A, k, i)

    ans = count = 1
    check = A[0]
    for i in range(1, n):
        if A[i] == check:
            count += 1
        else:
            ans = max(ans, count)
            count = 1
            check = A[i]

    ans = max(ans, count)  # checking last element cuz it never goes to else in loop
    return ans


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests(f, all_tests=True)
