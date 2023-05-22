from zad4testy import runtests
import queue

"""
First BFS finds the shortes path, next each edges is deleted from graph and BFS again looks for new shortes path 
(hopefully longer)
"""


def BFS(G: list, s: int, t: int) -> (int, list):
    Q = queue.Queue()
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [-1 for _ in range(n)]
    steps = [-1 for _ in range(n)]
    visited[s] = True
    steps[s] = 0
    Q.put(s)

    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if visited[v] is False:
                visited[v] = True
                parent[v] = u
                steps[v] = steps[u] + 1
                Q.put(v)

    return steps[t], parent


def get_path(parent: list, t: int) -> list:
    path = [t]
    while parent[t] != -1:
        t = parent[t]
        path.append(t)
    return path


def longer(G, s, t) -> (int, int):
    path_length, parent = BFS(G, s, t)
    if path_length == -1:
        return None
    path = get_path(parent, t)

    for i in range(1, len(path)):
        u = path[i - 1]
        v = path[i]

        G[u].remove(v)
        G[v].remove(u)

        new_length, _ = BFS(G, s, t)
        if new_length > path_length or new_length == -1:
            return u, v

        G[u].append(v)
        G[v].append(u)

    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
