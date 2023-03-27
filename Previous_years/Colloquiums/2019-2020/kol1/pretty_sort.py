from typing import List

"""
Solution requires converting array to contain counters of once and multiple appearance. Sorting with counting sorts
by multiple and than by once solve problem
"""


def countingsort(A: List[List[int]], k: int, index: int) -> None:
    n = len(A)
    C = [0] * k
    B = [None] * n

    for i in range(n):
        C[A[i][index]] += 1
    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(n - 1, -1, -1):
        C[A[i][index]] -= 1
        B[C[A[i][index]]] = A[i]

    for i in range(n):
        A[i] = B[i]


def countingsort2(A: List[List[int]], k: int, index: int) -> None:
    n = len(A)
    C = [0] * k
    B = [None] * n

    for i in range(n):
        C[A[i][index]] += 1
    for i in range(1, k):
        C[i] += C[i - 1]

    for i in range(n):
        C[A[i][index]] -= 1
        B[C[A[i][index]]] = A[i]

    for i in range(n):
        A[i] = B[n - i - 1]


def zad1(T: List[int]) -> None:
    arr = []
    kj = 0
    kw = 0
    for num in T:
        add = [0 for _ in range(11)]
        m = 10
        while m // 10 < num:
            tmp = int((num % m) // (m / 10))
            add[tmp] += 1
            m *= 10

        cj = 0
        cw = 0
        for l in add:
            if l == 1:
                cj += 1
            elif l != 0:
                cw += 1
            kj = max(kj, cj)
            kw = max(kw, cw)

        arr.append([num, cj, cw])

    countingsort(arr, kw + 1, 2)  # counting sort in multiple appearance
    countingsort2(arr, kj + 1, 1)  # counting sort by once appearance
    print(arr)
    for k in range(len(T)):
        T[k] = arr[k][0]


T = [2344, 1266, 123, 455, 114577, 67333, 32144]

print(T)
zad1(T)
print(T)
