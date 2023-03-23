from typing import List

# finds element that will be on k position after sort
# logn
def swap(A: List[int], i: int, j: int) -> None:
    A[i], A[j] = A[j], A[i]


def select(A: List[int], p: int, r: int, k: int) -> int:
    if p == r: return A[p]
    if p < r:
        q = partition(A, p, r)
        if q == k:
            return A[q]
        elif q < k:
            return select(A, q + 1, r, k)
        else:
            return select(A, p, q - 1, k)


def partition(A: List[int], p: int, r: int) -> int:
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1


arr = [1, 8, 2, 5, 4, 3, 7, 9, 10, 532, 125, 25, 24]
print(arr)
print(select(arr, 0, len(arr) - 1, 4))
print(arr)
