import math

from kol2testy import runtests

"""
Better solution

O(VE) solution
Sort list of edges by their cost, check first n-1 edges whether is MST with BFS or DFS if not remove 0 edge and add next 
edges from list till finding max MST
"""


def beautree(G: list) -> int:
    n = len(G)
    E = []

    for u in range(n):
        for v, w in G[u]:
            if u < v:
                E.append((u, v, w))

    E.sort(key=lambda x: x[2])
    G = [[] for _ in range(n)]

    def DFS() -> int:
        nonlocal n
        visited = [False for _ in range(n)]
        price = 0

        def DFS_visit(u: int) -> None:
            nonlocal price
            visited[u] = True
            for v, p in G[u]:
                if visited[v] is False:
                    price += p
                    DFS_visit(v)

        DFS_visit(0)

        for f in visited:
            if f is False:
                return None
        return price

    for u, v, p in E[:n - 2]:
        G[u].append((v, p))
        G[v].append((u, p))

    for i in range(n - 2, len(E)):
        u, v, p = E[i]
        G[u].append((v, p))
        G[v].append((u, p))
        result = DFS()

        if result is not None:
            return result

        u, v, p = E[i - n + 2]
        G[u].remove((v, p))
        G[v].remove((u, p))

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(beautree, all_tests=True)

G = [[(1, 3), (2, 1), (4, 2)],  # 0
     [(0, 3), (2, 5)],  # 1
     [(1, 5), (0, 1), (3, 6)],  # 2
     [(2, 6), (4, 4)],  # 3
     [(3, 4), (0, 2)]]  #

beautree(G)
