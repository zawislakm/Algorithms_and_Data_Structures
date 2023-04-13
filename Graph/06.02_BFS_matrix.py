import GraphTransformations as t
import queue

# BFS
# finds shortest paths
# test connectivity
# finding cycle
# O(V^2)

def BFS(G: list, s: int = 0) -> None:
    G = t.list_to_matrix(G)
    Q = queue.Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [-1 for _ in range(n)]
    distance[s] = 0
    visited[s] = True
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if visited[v] is False and G[u][v] == 1:
                visited[v] = True
                distance[v] = distance[u] + 1
                parent[v] = u
                Q.put(v)

    print("Distance: ", distance)
    print("Parents: ", parent)
    return None


simpleGraph = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12],
     [10, 11]]

BFS(simpleGraph)
