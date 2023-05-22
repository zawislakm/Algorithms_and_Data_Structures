import math
import GraphTransformations as GT


# O(V^2) V - vertices
def Dijkstra(M: list, s: int, t: int) -> int:
    M = GT.list_to_matrix_wages(M)
    n = len(M)
    weights = [10 ** 10 for _ in range(n)]
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    weights[s] = 0

    for _ in range(n):

        # pick vertice with the lowest weight
        u = -1
        min_distance = math.inf
        for j in range(n):
            if visited[j] is False and weights[j] < min_distance:
                min_distance = weights[j]
                u = j

        # relaxation
        visited[u] = True
        for v in range(n):
            if M[u][v] != 0 and visited[v] is False and weights[v] > weights[u] + M[u][v]:
                weights[v] = weights[u] + M[u][v]
                parent[v] = u

    print(weights)

    return weights[t]


dijkstraGraph = [[(1, 3), (8, 1), (3, 3)], [(0, 3), (2, 5)], [(1, 5), (3, 2), (5, 1)], [(0, 3), (2, 2), (4, 3), (6, 1)],
                 [(3, 3), (5, 8), (7, 1)], [(2, 1), (4, 8), (7, 4)], [(3, 1), (7, 7), (8, 2)], [(4, 1), (5, 4), (6, 7)],
                 [(0, 1), (6, 2)]]
s = 8
t = 5
Dijkstra(dijkstraGraph, s, t)
