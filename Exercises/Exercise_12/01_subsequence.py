"""
In arrays A and B of different lengths find a common subsequence
"""
"""
A - array size of n
B - array size of m

f(i, j) - the longest common subsequence of the strings A[1..i] and B[1..j]
f(0, j) = 0
f(i, 0) = 0
f(i, j) = {
              f(i - 1, j - 1) + 1, when A[i] == B[j],
              max(f(i - 1, j), f(i, j - 1)), when A[i] != B[j],
              0, when i == 0 lub j == 0
}
O(n*m)
"""


def subsequence(A: list, B: list):
    n = len(A)
    m = len(B)

    DP = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

    DP[0] = [0 for _ in range(m + 1)]
    for i in range(1, n + 1):
        DP[i][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            if A[i - 1] == B[j - 1]:
                DP[i][j] = DP[i - 1][j - 1] + 1
            else:
                DP[i][j] = max(DP[i - 1][j], DP[i][j - 1])

    def rek(i: int, j: int):
        # recursive version
        if i < 0 or j < 0:
            return 0

        if DP[i][j] != -1:
            return DP[i][j]

        if A[i - 1] == B[j - 1]:
            DP[i][j] = max(DP[i][j], rek(i - 1, j - 1) + 1)
        else:
            DP[i][j] = max(DP[i][j], rek(i - 1, j), rek(i, j - 1))

        return DP[i][j]

    # rek(n, m)

    sub = []

    def get_sub(i: int, j: int):

        if i < 0 or j < 0:
            return

        if DP[i][j] == 0:
            return

        if DP[i][j] != DP[i - 1][j]:
            sub.append(A[i - 1])
            get_sub(i - 1, j)
        else:
            if DP[i][j] == DP[i][j - 1]:
                get_sub(i, j - 1)
            else:
                get_sub(i - 1, j)

    get_sub(n, m)
    sub.reverse()
    print(f'Found maximum subsequence {sub}')

    return sub


A = [0, 7, 3, 0, 2, 9]
B = [3, 5, 1, 0, 7, 9, 11]

A1 = [3, 1, 2]
B1 = [3, 1, 4, 2]
subsequence(A, B)
