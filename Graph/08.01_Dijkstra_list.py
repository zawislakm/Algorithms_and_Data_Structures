import queue


# O(ElogV) E - edges V - vertices
def Dijkstra(G: list, s: int, t: int) -> int:
    n = len(G)
    visited = [False for _ in range(n)]
    weights = [10 ** 10 for _ in range(n)]
    weights[s] = 0
    Q = queue.PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        w, u = Q.get()
        if visited[u] is False:
            for v, p in G[u]:
                if visited[v] is False and weights[v] > w + p:
                    weights[v] = w + p
                    Q.put((w + p, v))
            visited[u] = True

    return weights[t]


dijkstraGraph = [[(1, 3), (8, 1), (3, 3)], [(0, 3), (2, 5)], [(1, 5), (3, 2), (5, 1)], [(0, 3), (2, 2), (4, 3), (6, 1)],
                 [(3, 3), (5, 8), (7, 1)], [(2, 1), (4, 8), (7, 4)], [(3, 1), (7, 7), (8, 2)], [(4, 1), (5, 4), (6, 7)],
                 [(0, 1), (6, 2)]]
s = 8
t = 5
Dijkstra(dijkstraGraph, s, t)
