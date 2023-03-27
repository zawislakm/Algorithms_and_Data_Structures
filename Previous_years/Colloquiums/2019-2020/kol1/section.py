from typing import List


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


def partition(A: List[int], p: int, r: int) -> int:
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def section(T: List[int], p: int, r: int) -> List[int]:
    select(T, r)
    select(T, p)
    # seems like selects sorts array from r to p
    return T[p:r + 1]

T = [37, 98, 175, 172, 143, 134, 172, 189, 210, 225, 179, 183, 152, 146]
#T = [3, 8, 7, 8, 4, 9, 5, 3, 8, 8, 8]
print(section(T, 3, 9))
