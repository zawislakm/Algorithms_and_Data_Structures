"""
Check whether given graph is bipartite graph
"""

"""
Simple BFS which sets opposite color than parent, when BFS meets visited vertex check whether is opposite color
"""

import queue


def BFS(G: list, s: int = 0) -> bool:
    n = len(G)
    visited = [False for _ in range(n)]
    color = [-1 for _ in range(n)]
    Q = queue.Queue()
    Q.put(s)
    color[s] = 0
    visited[s] = 0

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if visited[v] is False:
                visited[v] = True
                color[v] = 1 - color[u]
                Q.put(v)
            elif color[v] == color[u]:
                return False

    return True


simpleGraph = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12],
               [9, 12],
               [10, 11]]

simpleGraphAdd = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11],
                  [9, 11, 12],
                  [9, 10, 12],
                  [10, 11]] #edge between 10 and 11 added
print(BFS(simpleGraph))
print(BFS(simpleGraphAdd))
