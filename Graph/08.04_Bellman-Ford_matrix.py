import math
import GraphTransformations as GT

# 0 in matrix means no edge
# O(vE)
def BellmanFord(G: list, s: int):
    n = len(G)
    M = GT.list_to_matrix_wages(G)
    weights = [math.inf for _ in range(n)]
    parent = [None for _ in range(n)]
    weights[s] = 0

    for _ in range(n-1):
        for u in range(n):
            for v in range(n):
                if weights[u] != math.inf and M[u][v] != 0 and M[u][v] + weights[u] < weights[v]:
                    parent[v]=u
                    weights[v] = M[u][v] + weights[u]

    for u in range(n):
        for v in range(n):
            if weights[u] != math.inf and M[u][v] != 0 and weights[v] > M[u][v] + weights[u]:
                return None
    print(weights)

    return weights


dijkstraGraphModyfied = [[(1, -3), (8, 1), (3, 3)], [(0, 3)], [(3, 2), (5, 1)], [(0, 3), (2, 2), (4, 3), (6, 1)],
                 [(3, 3), (5, 8), (7, 1)], [(2, 1), (4, 8), (7, 4)], [(3, 1), (7, 7), (8, 2)], [(4, 1), (5, 4), (6, 7)],
                 [(0, 1), (6, 2)]]
s = 8

BellmanFord(dijkstraGraphModyfied,s)