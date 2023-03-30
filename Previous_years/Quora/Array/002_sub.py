from typing import List


def subarray(A: List[int]) -> bool:
    n = len(A)
    sub = [0 for _ in range(n)]
    sub[0] = A[0]

    for i in range(1, n):
        sub[i] = sub[i - 1] + A[i]

    for i in range(n):
        if sub[i] == 0:

            return True

    for i in range(n):
        for j in range(i + 1, n):
            if sub[j] - sub[i] == 0:

                return True
    return False


arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
print(subarray(arr))
