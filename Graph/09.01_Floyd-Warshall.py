import math

import GraphTransformations as GT


# O(v^3) v-vertices
# matrix is the best way to store it

def FloydWarshall(G: list, s: int = None, e: int = None):
    n = len(G)
    M = GT.list_to_matrix_wages(G)
    P = [[None for _ in range(n)] for _ in range(n)]  # parent

    for x in range(n):
        for y in range(n):
            if M[x][y] == 0 and x != y:
                M[x][y] = math.inf
            if x != y and M[x][y] > 0:
                P[x][y] = x

    for t in range(1, n + 1):
        for x in range(n):
            for y in range(n):
                if M[x][t - 1] + M[t - 1][y] < M[x][y]:
                    P[x][y] = P[t - 1][y]
                    M[x][y] = M[x][t - 1] + M[t - 1][y]

    if s is not None and e is not None and M[s][e] != math.inf:
        # finding path
        pointer = s
        path = []
        while pointer != None:
            path.append(pointer)
            pointer = P[e][pointer]

        return path


dijkstraGraph = [[(1, 3), (8, 1), (3, 3)], [(0, 3), (2, 5)], [(1, 5), (3, 2), (5, 1)], [(0, 3), (2, 2), (4, 3), (6, 1)],
                 [(3, 3), (5, 8), (7, 1)], [(2, 1), (4, 8), (7, 4)], [(3, 1), (7, 7), (8, 2)], [(4, 1), (5, 4), (6, 7)],
                 [(0, 1), (6, 2)]]

FloydWarshall(dijkstraGraph, 8, 7)
