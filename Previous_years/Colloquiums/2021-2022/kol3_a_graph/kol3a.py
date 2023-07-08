from kol3atesty import runtests

"""
New vertex as speciality of Bitalgo. Vertices from S array have edge with new vertex of cost 0. Dijkstra.
"""

INF = 10 ** 10
import queue


def spacetravel(n, E, S, a, b):

    for i in S:
        E.append((i, n, 0))
    n += 1

    G = [[] for _ in range(n)]

    for u, v, p in E:
        G[u].append((v, p))
        G[v].append((u, p))

    visited = [False for _ in range(n)]
    weight = [INF for _ in range(n)]
    weight[a] = 0
    Q = queue.PriorityQueue()
    Q.put((0, a))

    while not Q.empty():
        w, u = Q.get()

        for v, p in G[u]:
            if visited[v] is False and weight[v] > w + p:
                weight[v] = w + p
                Q.put((w + p, v))

        visited[u] = True


    if visited[b] is True:
        return weight[b]
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )

E = [(0, 1, 5),
     (1, 2, 21),
     (1, 3, 1),
     (2, 4, 7),
     (3, 4, 13),
     (3, 5, 16),
     (4, 6, 4),
     (5, 6, 1)]
S = [0, 2, 3]
a = 1
b = 5
n = 7

spacetravel(n, E, S, a, b)
