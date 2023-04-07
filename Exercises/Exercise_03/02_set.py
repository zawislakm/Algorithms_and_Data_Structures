"""
In given array A of length n are only logn different number. Sort it in n* log(logn))
n = 1024 only 10 different elements
"""

"""
Solution requires creating array working like dictt, to find all different elements. Than is just simple counting sort.
n*lon(logn)

It seams that normal quciksort would work only in n*lon(logn) with this type of data
"""

from math import log2
from typing import List


def binary_search(arr: List[int], target: int, l: int, r: int) -> int:
    mid = (l + r) // 2

    if mid == 0 or mid == len(arr) - 1:
        return mid
    if arr[mid - 1] < target and arr[mid - 1] != -1 and arr[mid] == -1:  # case [3,5,-1,-1], target = 9
        return mid
    if arr[mid - 1] < target and arr[mid] > target:  # case [3,5,-1,-1], target = 4
        return mid
    if arr[mid] == -1 or arr[mid - 1] > target:
        return binary_search(arr, target, l, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, r)


def put_in(dict: List[int], num: int) -> None:
    j = binary_search(dict, num, 0, len(dict) - 1)
    # moves everything right
    while j < len(dict) and num != -1:
        dict[j], num = num, dict[j]
        j += 1


def countingsort(A: List[int], dict: List[int], k: int) -> None:
    n = len(A)
    C = [[dict[i], 0] for i in range(k)]
    B = [0 for _ in range(n)]

    for x in A:
        for j in range(k):
            if dict[j] == x:
                C[j][1] += 1

    for i in range(1, k):
        C[i][1] = C[i][1] + C[i - 1][1]

    for i in range(n - 1, -1, -1):
        for j in range(k):
            if dict[j] == A[i]:
                B[C[j][1] - 1] = A[i]
                C[j][1] -= 1

    for i in range(n):
        A[i] = B[i]


def set_solution(A: List[int]) -> None:
    n = len(A)
    k = int(log2(n))
    dict = [-1 for _ in range(k)]  # I believe there is no -1 in A
    found = 0

    for x in A:
        if x not in dict:
            put_in(dict, x)
            found += 1
        if found == k:
            break

    countingsort(A, dict, k)


arr = [3, 1, 5, 12, 3, 3, 3, 1, 5, 12, 12, 5, 3, 1, 5, 12]
print(arr)
set_solution(arr)
print(arr)
