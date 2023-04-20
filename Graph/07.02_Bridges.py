# delete egde -> notcoherant grpah


def DFS(G: list) -> list:
    bridge = []
    n = len(G)
    time = 0
    visited = [False for _ in range(n)]
    times = [-1 for _ in range(n)]
    low = [-1 for _ in range(n)]

    def DFS_visit(u: int, p: int = -1) -> None:
        nonlocal time
        visited[u] = True
        time += 1
        times[u] = low[u] = time
        for v in G[u]:
            if v == p:
                continue
            if visited[v] is True:
                low[u] = min(low[u], times[v])
            else:
                DFS_visit(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > times[u]:
                    bridge.append((v, u))

    for u in range(n):
        if visited[u] is False:
            DFS_visit(u)

    return bridge


simpleGraph = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12],
               [9, 12],
               [10, 11]]

print(DFS(simpleGraph))
