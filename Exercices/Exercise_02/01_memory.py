"""
Optimize quicksort to use only O(logn) extra memory space
"""
from typing import List

"""
Using code from 03_02_Better_Quicksort, in while loop recursion is started from part of array that is shorter, longer
part continue working in while loop.
"""


def swap(A: List[int], i: int, j: int) -> None:
    A[i], A[j] = A[j], A[i]


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
        if A[j] <= x:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1


arr = [1, 8, 2, 5, 3, 7, 9,4]
print(arr)
quicksort(arr, 0, len(arr) - 1)
print(arr)