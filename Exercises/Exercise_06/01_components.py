"""
Count components in given graph (undirected)
"""

"""
Simple DFS with added counter in loop that starts DFS_visit
"""


def DFS(G: list) -> int:
    n = len(G)
    visited = [False for _ in range(n)]
    ans = 0

    def DFS_visit(u: int):
        visited[u] = True
        for v in G[u]:
            if visited[v] is False:
                DFS_visit(v)

    for u in range(n):
        if visited[u] is False:
            DFS_visit(u)
            ans += 1
    return ans


simpleGraph = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12],
               [9, 12],
               [10, 11]]

print(DFS(simpleGraph))
