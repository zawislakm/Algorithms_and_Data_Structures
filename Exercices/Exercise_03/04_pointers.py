"""
Find pointers to indexes which contains all type of number from given array, distance between this pointers should be
minimal
"""

"""
Solution requires creating pointers (i,j), counter of found numbers, addition array with zeros of length k 
(k is amount of different numbers) which will count found numbers between pointers (i,j).
While going through given array, j pointers move if not all number are found otherwise i moves.
  
"""

from typing import List


def find_pointer(A: List[int], k: int) -> (int, int):
    n = len(A)

    dict = [0 for _ in range(k)]
    found_colors = 0
    start = -1
    end = n + 1
    i = 0
    j = 0

    while j < n:
        if found_colors == k:

            dict[A[i]] -= 1
            if dict[A[i]] == 0:
                found_colors -= 1
            i += 1
            if found_colors == k and j - i < end - start:
                end = j
                start = i

        else:
            dict[A[j]] += 1
            if dict[A[j]] == 1:
                found_colors += 1

            if found_colors == k and j - i < end - start:
                end = j
                start = i

            j += 1

    if start == -1:
        return -1, -1

    print(arr[start:end])
    return start, end - 1


arr = [1, 2, 1, 4, 2, 1, 1, 0, 4, 3, 1, 2]
k = 5
print(find_pointer(arr, k))
