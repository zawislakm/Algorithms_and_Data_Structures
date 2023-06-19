import math

def city_distances(C: list) -> list:
    n = len(C)
    D = [[0 for _ in range(n)] for _ in range(n)]

    def distance_counter(x1, y1, x2, y2):
        return math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))

    for i in range(n):
        x1, y1 = C[i]
        for j in range(i + 1, n):
            x2, y2 = C[j]
            D[i][j] = D[j][i] = distance_counter(x1, y1, x2, y2)
    return D


def task(C: list) -> float:
    n = len(C)
    D = city_distances(C)
    F = [[float('inf') for _ in range(n)] for _ in range(n)]
    F[0][1] = D[0][1]

    def tspf(i: int, j: int) -> float:
        nonlocal F, D

        if F[i][j] != float('inf'):
            return F[i][j]

        if i == j - 1:
            best = float('inf')
            for k in range(j - 1):
                best = min(best, tspf(k, j - 1) + D[k][j])
            F[i][j] = best
        else:
            F[i][j] = tspf(i, j - 1) + D[j - 1][j]
        return F[i][j]

    minimum_distance = float('inf')

    for i in range(n - 1):
        minimum_distance = min(minimum_distance, tspf(i, n - 1) + D[i][n - 1])

    return minimum_distance


C = [(1, 0), (0, 6), (2, 3), (6, 1), (8, 2), (7, 5), (5, 4)]
print(task(C))
