"""
Check whether in undirected graph exists path from vertex x to vertex y, path requires using decreasing edge wages.
Wages values are from [1..N], where N is number of edges and all edges have different cost
"""

"""
Using BFS find way, add edges to queue in decreasing wages
"""
import queue
import math


def BFS(G: list, x: int, y: int) -> bool:
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    Q = queue.PriorityQueue()
    visited[x] = True
    Q.put((-1 * math.inf, x))

    while not Q.empty():
        w, u = Q.get()
        w *= -1
        G[u].sort(key=lambda x: x[1], reverse=True)

        for v, p in G[u]:
            if visited[v] is False and w > p:
                Q.put((-1 * p, v))
                parent[v] = u
        visited[u] = True

    if visited[y]:
        path = [y]
        u = parent[y]
        while u != -1:
            path.append(u)
            u = parent[u]
        path.reverse()
        print("Path: ", path)

    return visited[y]


G = [[(1, 2), (2, 8)], [(0, 2), (2, 6), (4, 1), (3, 5)], [(0, 8), (1, 6), (3, 9)], [(1, 5), (2, 9), (4, 4), (5, 7)],
     [(1, 1), (3, 4), (5, 3)], [(4, 3), (3, 7)]]
x = 0
y = 5
print(BFS(G, x, y))
