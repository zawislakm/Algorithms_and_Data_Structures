from zad1testy import runtests


def islands(G: list, A: int, B: int) -> int:
    # Dijkstra logic with remembering transportation
    n = len(G)
    visited = [False for _ in range(n)]
    weights = [10 ** 10 for _ in range(n)]
    transport = [-1 for _ in range(n)]

    weights[A] = 0

    for _ in range(n):

        u = -1
        best = float('inf')
        for v in range(n):
            if weights[v] < best and visited[v] is False:
                best = weights[v]
                u = v

        visited[u] = True
        for v in range(n):
            if visited[v] is False and G[u][v] != 0 and (transport[u] == -1 or transport[u] != G[u][v]) and weights[v] > \
                    weights[u] + G[u][v]:
                transport[v] = G[u][v]
                weights[v] = weights[u] + G[u][v]

    return weights[B]


runtests(islands)
