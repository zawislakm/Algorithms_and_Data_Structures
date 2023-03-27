from zad3testy import runtests
from typing import List

"""
P array is useless. To prevent possibility 1 in array P, simply use bucket sort than again bucket sort with insertion 
sort on bucket from first bucket sort calling
"""


def insertion_sort(arr: List[float]) -> None:
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key <= arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def bucket_sort_depth1(arr: List[float]) -> None:
    n = len(arr)
    min_e = min(arr)
    max_e = max(arr)

    if min_e == max_e:
        return

    buckets = [[] for _ in range(n + 1)]

    for x in arr:
        index = int((x - min_e) / (max_e - min_e) * n)
        buckets[index].append(x)
    print(buckets)
    for bucket in buckets:
        if len(bucket) > 1:
            bucket_sort_depth2(bucket)

    k = 0
    for bucket in buckets:
        for e in bucket:
            arr[k] = e
            k += 1


def bucket_sort_depth2(arr: List[float]) -> None:
    n = len(arr)
    min_e = min(arr)
    max_e = max(arr)

    if min_e == max_e:
        return

    buckets = [[] for _ in range(n + 1)]

    for x in arr:
        index = int((x - min_e) / (max_e - min_e) * n)
        buckets[index].append(x)

    for bucket in buckets:
        if bucket != []:
            insertion_sort(bucket)

    k = 0
    for bucket in buckets:
        for e in bucket:
            arr[k] = e
            k += 1


def SortTab(T, P):
    bucket_sort_depth1(T)
    return


runtests(SortTab)

