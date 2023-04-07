from kol1testy import runtests

"""
Algorithm creates array slice of p length, then picks k element from given slice using quickselect
O(np) 
"""


def quickselect(A: list, k: int, p: int = 0, r: int = None) -> int:
    if r is None:
        r = len(A) - 1
    if p == r:
        return A[p]
    if p < r:
        q = partition(A, p, r)
        if q == k:
            return A[q]
        elif q < k:
            return quickselect(A, k, q + 1, r)
        else:
            return quickselect(A, k, p, q - 1)


def partition(A: list, p: int, r: int) -> int:
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def ksum(T: list, k: int, p: int) -> int:
    n = len(T)
    ans = 0

    for i in range(n - p + 1):
        arr_slice = T[i:i + p]
        ans += quickselect(arr_slice, k - 1)
    return ans


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=False)
