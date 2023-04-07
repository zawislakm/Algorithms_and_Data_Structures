"""
In not sorted array is serval cases of inversion ( i < j, but arr[i] > arr[j]), find way to count all inversions
"""

"""
Easy way is to do it during mergesort, having sorted left_arr and right_arr array, while creating return array when
element on right array is smaller it means all remaining elements on left array have inversion with this element

Test cases:
[1, 3, 5, 7, 10, 4, 6, 8, 9]  # 3 -> [2] 5-> [2,4] 7->[2,4,6] 10->[2,4,6,8,9]
[2, 3, 1, 4, 6, 5]  # 2-> [1] 3-> [1] 6-> [5]
[7, 3, 8, 5, 2, 1]  # 7-> [3,5,2,1] 3-> [2,1] 8->[5,2,1] 5-> [2,1] 2->[1]
"""
# nlogn
from typing import List


def count_inversion(arr: List[int]) -> int:
    if len(arr) == 1 or len(arr) == 0:
        return 0
    n = len(arr)
    mid = n // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]
    ans = 0
    ans += count_inversion(left_arr)
    ans += count_inversion(right_arr)

    i = j = k = 0
    while i < len(left_arr) and j < len(right_arr):

        if left_arr[i] <= right_arr[j]:

            arr[k] = left_arr[i]
            i += 1
        else:
            ans += mid - i
            # inversion count here
            # from first case: 3 and 2, inversion it means that all elements behind 3 also have this inversion
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

    return ans


test_0 = [1, 3, 5, 7, 10, 4, 6, 8, 9]  # 3 -> [2] 5-> [2,4] 7->[2,4,6] 10->[2,4,6,8,9]
test_1 = [2, 3, 1, 4, 6, 5]  # 2-> [1] 3-> [1] 6-> [5]
test_2 = [7, 3, 8, 5, 2, 1]  # 7-> [3,5,2,1] 3-> [2,1] 8->[5,2,1] 5-> [2,1] 2->[1]

print(count_inversion(test_0))
