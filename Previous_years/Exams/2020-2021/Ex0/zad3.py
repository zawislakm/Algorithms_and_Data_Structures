import queue

# both solutions are (n^3)
def jumper(M: list, s: int, w: int) -> int:
    n = len(M)
    G = [[] for _ in range(n)]
    for u in range(n):
        for v in range(n):
            if M[u][v] > 0:
                G[u].append((v, M[u][v]))

    print(f"Graph: {G}")

    visited = [[False for _ in range(2)] for _ in range(n)]
    weights = [[float('inf') for _ in range(2)] for _ in range(n)]
    weights[s] = [0, 0]
    visited[s] = [True, True]
    Q = queue.PriorityQueue()
    Q.put((0, s, True))  # true, boots are available

    while not Q.empty():
        p, u, boots = Q.get()

        if boots is True:
            for v1, w1 in G[u]:
                for v2, w2 in G[v1]:
                    if visited[v2][1] is False and weights[v2][1] > max(w1, w2) + p:
                        weights[v2][1] = max(w1, w2) + p
                        Q.put((weights[v2][1], v2, False))

        for v1, w1 in G[u]:
            if visited[v1][0] is False and weights[v1][0] > w1 + p:
                weights[v1][0] = w1 + p
                Q.put((weights[v1][0], v1, True))

        visited[u][boots] = True
    for i in weights:
        print(i)

    return min(weights[w])


def jumper1(G, s, w):
    n = len(G)

    visited = [[False for _ in range(2)] for _ in range(n)]
    weights = [[float('inf') for _ in range(2)] for _ in range(n)]
    weights[s] = [0, 0]

    for _ in range(2 * n):  # 2 times, cuz nodes are multiple by 2

        boots = -1
        u = -1
        lowest = float('inf')
        for v in range(n):
            for i in range(2):
                if visited[v][i] is False and lowest > weights[v][i]:
                    boots = i
                    u = v
                    lowest = weights[v][i]
        visited[u][boots] = True
        for v in range(n):
            if visited[v][0] is False and weights[v][0] > weights[u][boots] + G[u][v] and G[u][v] > 0:
                weights[v][0] = weights[u][boots] + G[u][v]

        if boots == 0:
            for v in range(n):
                if G[u][v] > 0:
                    for k in range(n):

                        if visited[k][1] is False and weights[k][1] > weights[u][boots] + max(G[u][v], G[v][k]) and \
                                G[v][k] > 0:
                            weights[k][1] = weights[u][boots] + max(G[u][v], G[v][k])


    return min(weights[w])


G = [[-1, 1, 0, 0, 0], [1, -1, 1, 0, 0], [0, 1, -1, 7, 0], [0, 0, 7, -1, 8], [0, 0, 0, 8, -1]]
s = 0
w = 4
print(jumper1(G, s, w))
