"""
Undirected graph with weight of edges from set (1 to E), all weight different. Find minimal path from s to t, using
only decreasing weight of edges.
"""

"""
Modified dijkstra algorythem
"""
import queue

INF = 10 ** 10


def small(G: list, s: int, t: int) -> int:
    n = len(G)
    max_element = 0
    for u in range(n):
        for _, p in G[u]:
            max_element = max(max_element, p)
    p = max_element
    visited = [[False for _ in range(p + 1)] for _ in range(n)]
    weight = [[INF for _ in range(p + 1)] for _ in range(n)]
    parent = [[[-1, -1] for _ in range(p + 1)] for _ in range(n)]
    Q = queue.PriorityQueue()
    weight[s][0] = 0
    visited[s] = [True for _ in range(p + 1)]
    Q.put((0, INF, s))

    while not Q.empty():
        w, last, u = Q.get()

        for v, p in G[u]:
            if visited[v][p] is False and weight[v][p] > w + p and last > p:
                weight[v][p] = w + p
                parent[v][p] = [u, last]
                Q.put((w + p, p, v))
        if last != INF:
            visited[u][last] = True

    if True in visited[t]:
        min_index = weight[t].index(min(weight[t]))
        path = [t]
        vertex_pointer, edge_pointer = parent[t][min_index]

        while vertex_pointer != -1 and edge_pointer != INF:
            path.append(vertex_pointer)
            print(vertex_pointer, edge_pointer)
            vertex_pointer, edge_pointer = parent[vertex_pointer][edge_pointer]
        path.append(s)
        path.reverse()
        print(f'Found path is {path}, with cost equal {weight[t][min_index]}')

        return weight[t][min_index]
    return -1


G = [[(1, 2), (2, 8)], [(0, 2), (2, 6), (4, 1), (3, 5)], [(0, 8), (1, 6), (3, 9)], [(1, 5), (2, 9), (4, 4), (5, 7)],
     [(1, 1), (3, 4), (5, 3)], [(4, 3), (3, 7)]]
x = 0
y = 5
small(G, x, y)
