"""
Given array A with number and given number T. Check whether it is possible to find
subsequence in A with sum equal to T
"""


def sub_sum(A: list, T: int) -> bool:
    A = list(filter(lambda x: x < T, A))
    print(A)
    n = len(A)
    DP = [[False for _ in range(T + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        DP[i][0] = True

    for i in range(1, n + 1):

        for j in range(1, T + 1):

            if A[i - 1] > j:
                DP[i][j] = DP[i - 1][j]

            else:
                DP[i][j] = (DP[i - 1][j] or DP[i - 1][j - A[i - 1]])

    return DP[n][T]


T = 8
A = [1, 2, 7, 4, 3, 3, 10]
print(sub_sum(A, T))
