"""
There is a ferry with two decks with both size of L. Find the maximum number of cars to fit on the ferry. Cars are
allowed to go on boat in given order, forbidden is skipping any vehicle.
"""
import math

"""
F(g,d,i) = True when the first and cars can be separated so that on the top deck they occupy length g and on the bottom deck d
F(g,d,i) = False in the opposite case

O(L^2n) 

this can be worked out to
F(g,i) and calculate d on the basis of information about the main deck and the sum of cars, then it will be
O(Ln)

"""

# try to return where car goes

def ferry(A: list, L: int):
    n = len(A)

    DP = [[[-math.inf for _ in range(L + 1)] for _ in range(L + 1)] for _ in range(n)]

    # for i in range(L): # work with out it?
    #     for j in range(L):
    #         DP[0][i][j] = 0

    def solve(i: int, j: int, k: int):
        if DP[i][j][k] != -math.inf:
            return DP[i][j][k]

        a = b = 0
        if A[i] <= j:
            a = solve(i + 1, j - A[i], k) + 1
        if A[i] <= k:
            b = solve(i + 1, j, k - A[i]) + 1

        DP[i][j][k] = max(a, b)
        return DP[i][j][k]

    solve(0, L, L)
    return solve(0, L, L)


A = [1, 1, 2, 3, 5, 8, 13]
L = 8
print(ferry(A,L))