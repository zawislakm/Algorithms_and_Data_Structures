# dag - directed acyclic graph
# topology sort sets vertices that edges points only from left to right
# can be used to determine order of tasks


def DFS(G: list) -> list:
    n = len(G)
    visited = [False for _ in range(n)]
    topSort = []

    def DFS_visit(u: int) -> None:
        visited[u] = True
        for v in G[u]:
            if visited[v] is False:
                DFS_visit(v)
        topSort.append(u)

    for u in range(n):
        if visited[u] is False:
            DFS_visit(u)

    topSort.reverse()
    print("Topology sort: ", topSort)
    return topSort


dagGraph = [[1, 2], [2, 3], [], [4, 5], [], [], [3]]
DFS(dagGraph)
