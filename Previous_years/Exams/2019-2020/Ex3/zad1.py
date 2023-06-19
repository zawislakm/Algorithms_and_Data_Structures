from zad1testy import runtests
import queue


def find_max(distances: list) -> int:
    n = len(distances)
    best = 0
    u = -1
    for v in range(n):
        if distances[v] > best:
            u = v
            best = distances[v]
    return u


def BFS_logic(G, s=0) -> (list, list):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [None for _ in range(n)]
    parent = [None for _ in range(n)]

    visited[s] = True
    distance[s] = 0
    Q = queue.Queue()
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if visited[v] is False:
                visited[v] = True
                Q.put(v)
                distance[v] = distance[u] + 1
                parent[v] = u

    return distance, parent


def best_root(L: list) -> int:
    # Simple find root of tree
    first_distance, _ = BFS_logic(L)
    first_leaf = find_max(first_distance)

    second_distance, parent = BFS_logic(L, first_leaf)
    second_leaf = find_max(second_distance)

    # Find middle of path between first and second leaf
    path = []
    while second_leaf != None:
        path.append(second_leaf)
        second_leaf = parent[second_leaf]



    return path[len(path)//2]


runtests(best_root)

L = [[2],
     [2],
     [0, 1, 3],
     [2, 4],
     [3, 5, 6],
     [4],
     [4]]

best_root(L)
