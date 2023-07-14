"""
Minimal cost of moving from the upper left corner of the chessboard to the lower right corner
"""

"""
f(i,j) = minimal cost of reaching position (i,j)
f(i,j) = C[i][j] + min(f(i-1,j),f(i,j-1)

remembering the boundary conditions, 
i <0 or j <0
return INF

i and j are field coordinates
"""

from math import inf


def chess(C: list) -> list:
    n = len(C)
    DP = [[inf for _ in range(n)] for _ in range(n)]
    parent = [[[-1, -1] for _ in range(n)] for _ in range(n)]
    DP[0][0] = C[0][0]
    for i in range(1, n):
        DP[0][i] = C[0][i] + DP[0][i - 1]
        DP[i][0] = C[i][0] + DP[i - 1][0]
        parent[0][i] = [0, i - 1]
        parent[i][0] = [i - 1, 0]

    for i in range(1, n):
        for j in range(1, n):
            if DP[i - 1][j] < DP[i][j - 1]:
                DP[i][j] = C[i][j] + DP[i - 1][j]
                parent[i][j] = [i - 1, j]
            else:
                DP[i][j] = C[i][j] + DP[i][j - 1]
                parent[i][j] = [i, j - 1]

    path = [(n - 1, n - 1)]

    i, j = parent[n - 1][n - 1]

    while i != -1 and j != -1:
        path.append((i, j))
        i, j = parent[i][j]
    path.reverse()

    print(f'Minimal cost is {DP[n - 1][n - 1]}, with path {path}')
    return path


C = [[3, 7, 1, 2], [7, 3, 4, 1], [4, 1, 7, 2], [3, 3, 8, 3]]
chess(C)
