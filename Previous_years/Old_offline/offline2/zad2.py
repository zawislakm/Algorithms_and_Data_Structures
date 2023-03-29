from typing import List

from zad2testy import runtests

"""
"""


def quciksort(A: List[List[int]], p1: int, p2: int, l: int = 0, r: int = None) -> None:
    # p1 and p2 way to sort List
    if r is None:
        r = len(A) - 1
    if l < r:
        p = partition(A, p1, p2, l, r)
        quciksort(A, p1, p2, l, p - 1)
        quciksort(A, p1, p2, p + 1, r)


def partition(A: List[List[int]], p1: int, p2: int, l: int, r: int) -> int:
    i = l - 1
    pivot = A[r][p1]
    pivot_2 = A[r][p2]
    for j in range(l, r):
        if A[j][p1] == pivot:
            if A[j][p2] > pivot_2:
                i += 1
                A[i], A[j] = A[j], A[i]
        elif A[j][p1] < pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1


def binary_search_bot(nums: List[List[int]], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid][1] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return left


def binary_search_pop(arr: List[List[int]], target: List[int], l: int = 0, r: int = None) -> None:
    # pops out from L_end array given target
    if r is None:
        r = len(arr) - 1

    mid = (r + l) // 2
    if arr[mid] == target:
        arr.pop(mid)
        return
    elif arr[mid][1] == target[1]:
        if arr[mid][0] > target[0]:
            return binary_search_pop(arr, target, mid + 1, r)
        else:  # change of way, cuz L_end after sort looks like this : [[2, 5], [5, 6], [1, 6], [1, 6], [8, 9]]
            return binary_search_pop(arr, target, l, mid - 1)

    elif arr[mid][1] > target[1]:
        return binary_search_pop(arr, target, l, mid - 1)
    else:
        return binary_search_pop(arr, target, mid + 1, r)


def depth(L: List[List[int]]) -> int:
    n = len(L)
    L_end = L.copy()

    quciksort(L, 0, 1)  # sort L first
    quciksort(L_end, 1, 0)
    ans = 0
    for i in range(n):
        binary_search_pop(L_end, L[i], 0, len(L_end) - 1)  # delete now looked element from L_end element
        ans = max(ans, binary_search_bot(L_end, L[i][1]))  # counts elements with end value <= L[i][1]

    return ans


runtests(depth)
