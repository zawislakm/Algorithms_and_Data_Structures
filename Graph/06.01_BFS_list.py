import queue

# BFS
# finds shortest paths
# test connectivity
# finding cycle
# O(V+E) V = vertices, E = edges

def BFS(G: list, s: int = 0) -> None:
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
        for v in G[u]:
            if visited[v] is False:
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
