import GraphTransformations as t


# visit all edges only once
# Undirected, coherent graph have Euler cycle when all vertexes have even
# start in random vertex, and go on to random not used edge

# O(V+E) list graph
# O(V^2) matrix graph

def DFS(G: list, s: int = 0) -> list:
    n = len(G)
    path = []
    G = t.list_to_matrix(G)

    last_used = [-1 for _ in range(n)]

    # array that remember last checked vertex, prevents:
    # O(V^2 + VE) list graph
    # O(V^3) matrix graph

    def DFS_visit(u):
        for v in range(last_used[u] + 1, n):
            if G[u][v] == 1:
                G[u][v] = 0
                G[v][u] = 0
                DFS_visit(v)
                last_used[u] = v
        path.append(u)

    DFS_visit(s)
    path.reverse()
    print("Path:", path)
    return path


eulerGraph = [[1, 2], [0, 2, 3, 4, 5, 6], [0, 1, 3, 4, 5, 6], [1, 2, 4, 5], [1, 2, 3, 5], [1, 2, 3, 4], [1, 2]]
DFS(eulerGraph)
