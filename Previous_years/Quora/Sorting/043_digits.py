def quicksort(A: list, p: int = 0, r: int = None) -> None:
    if r is None:
        r = len(A) - 1
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A: list, p: int, r: int) -> int:
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def digits(A: list) -> (int, int):
    n = len(A)
    d1 = 0
    d2 = 0
    quicksort(A)

    for i in range(0, n, 2):
        d1 *= 10
        d1 += A[i]

    for i in range(1,n,2):
        d2 *= 10
        d2 += A[i]

    return d1, d2


array = [ 9, 2, 5, 6, 0 ]
# 962 + 50 = 950 + 62 quick math
print(digits(array))
