# DFS
# test connectivity
# finding cycle
# topology sort
# Euler cycle
# finding articulation points/ bridges
# O(V+E)
def DFS(G: list) -> None:
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    time = 0
    times = [-1 for _ in range(n)]

    def DFS_visit(u: int) -> None:
        nonlocal time
        time += 1

        visited[u] = True
        for v in G[u]:
            if visited[v] is False:
                parent[v] = u
                DFS_visit(v)
        time += 1
        times[u] = time

    for u in range(n):
        if visited[u] is False:
            DFS_visit(u)

    print("Times: ", times)
    print("Parents: ", parent)


simpleGraph = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12],
     [10, 11]]

DFS(simpleGraph)
