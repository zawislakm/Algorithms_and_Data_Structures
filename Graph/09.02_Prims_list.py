import queue
import math


# O(ElogV)
# if weights are <0, just add the lowest value to all and solve MST (mst has always v-1 edges)


def Prims(G: list, s: int = 0):
    n = len(G)
    visited = [False for _ in range(n)]
    weights = [math.inf for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = queue.PriorityQueue()
    weights[s] = 0
    Q.put((0, s))

    while not Q.empty():
        w, u = Q.get()
        visited[u] = True
        for v, p in G[u]:
            if visited[v] is False and weights[v] > p:
                weights[v] = p
                parent[v] = u
                Q.put((p, v))


    print("Parent: ", parent)


mstGraph = [[(1, 1), (4, 5), (5, 8)], [(0, 1), (2, 3)], [(1, 2), (4, 4), (3, 6)], [(2, 6), (4, 2)],
            [(0, 4), (2, 4), (3, 2), (5, 7)], [(0, 8), (4, 7)]]
Prims(mstGraph)
