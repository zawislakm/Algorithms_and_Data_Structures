"""
Connect segments
Two segments are allowed to connect if they have exactly one point of intersection,
such as (1,4) and (4,5).

Several versions of the task:
1. whether it is possible to obtain the segment [a,b] (passed) by concatenating some of the segments
2. as above, but using only k segments
3. as above, but each segment has a positive price and minimize the sum of the prices of the glued segments
4. Calculate what is the longest segment that can be obtained by gluing at most k segments.
"""

"""
1. Make it graph out of it and use BFS
2. BFS, remember already done moves
3. Dijkstra

4. Other way?
"""
import queue


def make_graph(B: list) -> (list, int, int):
    # directed graph
    low = 10 * 10
    high = 0
    for u, v, _ in B:
        low = min(low, u, v)
        high = max(high, u, v)

    G = [[] for _ in range(high - low + 1)]

    for u, v, w in B:
        G[u - low].append((v - low, w))

    return G, low, high


def task1(B: list, a: int, b: int) -> bool:
    # Find path in graph
    G, low, high = make_graph(B)
    n = high - low + 1
    visited = [False for _ in range(n)]
    Q = queue.Queue()
    Q.put(a - low)
    visited[a - low] = True
    while not Q.empty():
        u = Q.get()
        for v, _ in G[u]:
            if visited[v] is False:
                Q.put(v)
                visited[v] = True

    return visited[b - low]


def task2(B: list, a: int, b: int, k: int) -> bool:
    # Find path in graph with BFS and find whether is shorter than k
    G, low, high = make_graph(B)
    n = high - low + 1
    visited = [False for _ in range(n)]
    time = [-1 for _ in range(n)]
    Q = queue.Queue()
    Q.put(a - low)
    visited[a - low] = True
    time[a - low] = 0
    while not Q.empty():
        u = Q.get()
        for v, _ in G[u]:
            if visited[v] is False:
                Q.put(v)
                visited[v] = True
                time[v] = time[u] + 1

    return visited[b - low] and time[b - low] <= k


def task3(B: list, a: list, b: list, k: int) -> bool:
    # Dijkstra on graph
    G, low, high = make_graph(B)
    n = len(G)
    Q = queue.PriorityQueue()
    visited = [False for _ in range(n)]
    weight = [10 ** 10 for _ in range(n)]
    visited[a - low] = True
    weight[a - low] = True
    Q.put((0, a - low))

    while not Q.empty():
        w, u = Q.get()
        for v, p in G[u]:
            if visited[v] is False and weight[v] > w + p:
                weight[v] = w + p
                Q.put((w + p, v))
        visited[u] = True

    return visited[b - low] and weight[b - low] <= k


B = [(1, 3, 3), (3, 6, 5), (6, 7, 1), (7, 8, 9), (2, 5, 2), (5, 7, 4)]
a = 1
b = 7
k = 8
print(task3(B, a, b, k))
