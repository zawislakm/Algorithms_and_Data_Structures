from zad2testy import runtests
from typing import List

"""
Maksymilian Zawiślak, 410609
Algorithm sorts given array (ravine) in decreasing order and sums elements minus index (past days,snow melt down)
in the sorted array, till its higher than 0.  

[1,7,3,4,1], snow = 7 (from index 1, from left side)
[0,0,2,3,0], snow = 3 (from index 3, from right side)
[0,0,1,0,0], snow = 1 (from index 2, both side access)
sum = 11

[1,7,3,4,1], snow = 4 (from index 3, from right side)
[0,6,2,0,0], snow = 6 (from index 1, from left side)
[0,0,1,0,0], snow = 1 (from index 2, both side access)
sum = 11

Sorted array:
[7,4,3,1,1], snow = 7 ,day = 0
[0,3,2,0,0], snow = 3 ,day = 1
[0,0,1,0,0], snow = 1 ,day = 2
sum = 11

"""


def quicksort(A: List[int], p: int, r: int) -> None:
    while p < r:
        q = partition(A, p, r)
        if q - p < r - q:
            quicksort(A, p, q - 1)
            p = q + 1
        else:
            quicksort(A, q + 1, r)
            r = q - 1


def partition(A: List[int], p: int, r: int) -> int:
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def snow(S: List[int]) -> int:
    quicksort(S, 0, len(S) - 1)
    snow_for_servers = 0
    i = 0
    while S[i] - i > 0:
        snow_for_servers += S[i] - i
        i += 1

    return snow_for_servers


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=False)
