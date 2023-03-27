from zad1testy import runtests
from typing import List

"""
Easy solution is to flat given array and use quick select. Just get index pointers to lower than diagonal,
pointers to elements on diagonal and higher then diagonal. Make loop 
"""


def select(A: List[int], k: int, p: int = 0, r: int = None) -> int:
    if r is None:
        r = len(A) - 1
    if p == r:
        return A[p]
    if p < r:
        q = partition(A, p, r)
        if q == k:
            return A[q]
        elif q < k:
            return select(A, k, q + 1, r)
        else:
            return select(A, k, p, q - 1)


def partition(A: List[int], p: int, r: int):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def Median(T: List[List[int]]) -> List[List[int]]:
    n = len(T)
    arr = []
    for l in T:
        for e in l:
            arr.append(e)

    amount = int((n * n - n) / 2)  # amount of low and high, there is always n mid elements
    # check on n = 2 and n = 3
    low = 0
    mid = low + amount
    high = mid + n

    for i in range(n):
        for j in range(n):
            if i > j:
                T[i][j] = select(arr, low)
                low += 1
            elif i == j:
                T[i][j] = select(arr, mid)
                mid += 1
            else:
                T[i][j] = select(arr, high)
                high += 1

    return T


runtests(Median)
