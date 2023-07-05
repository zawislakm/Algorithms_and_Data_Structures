from kolutesty import runtests
"""
Quicksort but it stops sorting when pivot minus index was higher than 0 with left side of array
or pivot minus index was smaller then 0 of right side of array. It gives O(n) I believe.
It sorts only parts where are numbers minus their index can be over or under 0.
Than just simple while loop on elements - minus their index till they are above 0.
"""

def swap(A: list, i: int, j: int) -> None:
    A[i], A[j] = A[j], A[i]


def quicksort(A: list, p: int = 0, r: int = None) -> None:
    if r is None:
        r = len(A) - 1
    if p < r:
        q = partition(A, p, r)
        if not A[q] - q >= 0:
            quicksort(A, p, q - 1)
        if not A[q] - q <= 0:
            quicksort(A, q + 1, r)


def partition(A: list, p: int, r: int) -> int:
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            swap(A, i, j)
    swap(A, i + 1, r)
    return i + 1


def ice_cream(T):
    quicksort(T)

    s = 0
    i = 0

    while T[i] - i > 0:
        s += T[i] - i
        i += 1

    return s


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ice_cream, all_tests=True)
