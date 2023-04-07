"""
In linear time sort array of length n with numbers from range [0,n^2-1]
"""

"""
Solution needs to use radix sort and counting sort, firstly given array needs to be extended, new array should have
[[given_number, given_number // n, given_number%n],...], then with using counting sort it should be sorted firstly with 
% result, then with //
"""

from typing import List


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


def radix_sort(arr: List[int]) -> None:
    k = len(arr)

    temporary_arr = [[x, x // k, x % k] for x in arr]
    print(temporary_arr)
    for index in range(2, 0, -1):
        countingsort(temporary_arr, k, index)

    for i in range(k):
        arr[i] = temporary_arr[i][0]


# 0 - 255

arr = [107, 70, 73, 45, 227, 229, 95, 157, 137, 12, 0, 225, 108, 49, 82, 143]
print(arr)
radix_sort(arr)
print(arr)
