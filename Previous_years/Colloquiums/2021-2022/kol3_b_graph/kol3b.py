from kol3btesty import runtests

INF = 10 ** 10
"""
New vertex as  "international airport". Vertices have edge with new vertex of cost from A table. Dijkstra.
"""

def airports(G, A, s, t):
    n = len(G)

    H = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for u in range(n):
        H[u][n] = H[n][u] = A[u]
        for v, p in G[u]:
            H[u][v] = p
    n += 1

    visited = [False for _ in range(n)]
    weight = [INF for _ in range(n)]
    weight[s] = 0

    for _ in range(n):

        best = index = INF
        for u in range(n):
            if visited[u] is False and weight[u] < best:
                best = weight[u]
                index = u

        u = index

        for v in range(n):
            if H[u][v] > 0 and visited[v] is False and weight[v] > H[u][v] + weight[u]:
                weight[v] = H[u][v] + weight[u]

        visited[u] = True

    return weight[t]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(airports, all_tests=True)

G = [[(1, 3), (3, 2)], [(0, 3), (2, 20)], [(1, 20), (5, 1), (3, 6)], [(0, 2), (2, 6), (4, 1)], [(3, 1), (5, 7)],
     [(4, 7), (2, 1)]]
S = [50, 100, 1, 20, 2, 70]
s = 0
t = 5
airports(G, S, s, t)
