from kol1testy import runtests

"""
Maksymilian Zawiślak, 410609
Algorytm idzie po zadanej petli i wyznacza przedzialy dlugosci p (tablica tmp) potem dla właśnie tej tabeli odplany
jest quickselect, który zwaraca wartość k-ty elementu z przedziału czego oczekujemy w zadaniu. Wyniki są sumowane.

O(np) czasowa
O(p) pamieci dodatkowej
"""


def quickselect(A: list, k: int, p: int, r: int) -> int:
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


def ksum(T, k, p):
    n = len(T)
    sum = 0

    for i in range(n - p + 1):
        tmp = T[i:i + p]
        sum += quickselect(tmp, k - 1, 0, len(tmp) - 1)
    return sum




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(ksum, all_tests=True)
