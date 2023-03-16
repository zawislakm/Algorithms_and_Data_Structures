from typing import List

# nlogn
def swap(A: List[int], i: int, j: int) -> None:
    A[i], A[j] = A[j], A[i]


def quicksort(A: List[int], p: int, r: int) -> None:
    while p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        p = q + 1


def partition(A: List[int], p: int, r: int) -> int:
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1


arr = [1, 8, 2, 5, 4, 3, 7, 9]
print(arr)
quicksort(arr, 0, len(arr) - 1)
print(arr)
