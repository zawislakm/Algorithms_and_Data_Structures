import math
import GraphTransformations as GT


# O(V^2)
# if weights are <0, just add the lowest value to all and solve MST (mst has always v-1 edges)


def Prims(G: list, s: int = 0):
    n = len(G)
    M = GT.list_to_matrix_wages(G)

    visited = [False for _ in range(n)]
    weights = [math.inf for _ in range(n)]
    parent = [None for _ in range(n)]
    weights[s] = 0

    for _ in range(n + 1):
        u = -1
        p = math.inf
        for v in range(n):
            if visited[v] is False and weights[v] < p:
                p = weights[v]
                u = v
        visited[u] = True

        for v in range(n):
            if visited[v] is False and weights[v] > M[u][v] and M[u][v] != 0:
                weights[v] = M[u][v]
                parent[v] = u

    print("Weights: ", weights)
    print("Parent: ", parent)


mstGraph = [[(1, 1), (4, 5), (5, 8)], [(0, 1), (2, 3)], [(1, 2), (4, 4), (3, 6)], [(2, 6), (4, 2)],
            [(0, 4), (2, 4), (3, 2), (5, 7)], [(0, 8), (4, 7)]]
Prims(mstGraph)
