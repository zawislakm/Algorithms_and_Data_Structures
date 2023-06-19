import math

from zad2testy import runtests


def FloydWarshall(G: list):
    n = len(G)
    for i in range(n):
        for j in range(n):
            if G[i][j] == 0 and i != j:
                G[i][j] = math.inf

    for k in range(1, n + 1):
        for u in range(n):
            for v in range(n):
                G[u][v] = min(G[u][v], G[u][k - 1] + G[k - 1][v])


def let(ch): return ord(ch) - ord("a")


def letters(G: list, W: list) -> int:
    # tu prosze wpisac swoje rozwiazanie
    L, E = G

    n = 0
    for u, v, _ in E:
        n = max(u, v, n)
    n += 1

    G = [[0 for _ in range(n)] for _ in range(n)]

    for u, v, p in E:
        G[u][v] = p
        G[v][u] = p

    FloydWarshall(G)

    word = [[] for _ in range(len(W))]

    for i in range(len(W)):
        l = W[i]
        for j in range(len(L)):

            if L[j] == l:
                word[i].append(j)

    ans = float('inf')

    def recurrsion(u: int, i: int = 1, num: int = 0) -> None:
        if i == len(W):
            nonlocal ans
            ans = min(ans, num)
            return
        for v in word[i]:
            recurrsion(v, i + 1, num + G[u][v])

    for u in word[0]:
        recurrsion(u)

    if ans == float('inf'):
        return -1
    return ans


runtests(letters)

G = (['k', 'k', 'o', 'o', 't', 't'], [(0, 2, 2), (1, 2, 1), (1, 4, 3), (1, 3, 2), (2, 4, 5), (3, 4, 1), (3, 5, 3)])
W = "kto"
letters(G, W)
