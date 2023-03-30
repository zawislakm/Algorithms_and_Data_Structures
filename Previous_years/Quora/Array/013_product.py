from typing import List, Tuple


def quicksort(A: List[int], p: int = 0, r: int = None):
    if r is None:
        r = len(A) - 1
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A: List[int], p: int, r: int) -> int:
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def find_product(A: List[int]) -> Tuple[int, int]:
    n = len(A)
    if n < 1:
        return -1, -1
    quicksort(A)

    if A[0] * A[1] >= A[n - 1] * A[n - 2]:
        return A[0], A[1]
    else:
        return A[n - 1], A[n - 2]


array = [-10, -3, 5, 6, -2]
print(find_product(array))
