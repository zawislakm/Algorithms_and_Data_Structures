from typing import List

# nlogn

def merge_sort(arr: List[int]):
    if len(arr) == 1 or len(arr) == 0:
        return

    n = len(arr)
    mid = n // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):

        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


arr = [1, 8, 2, 5, 4, 3, 7, 9]
print(arr)
merge_sort(arr)
print(arr)
