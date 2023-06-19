# W - weight, P - price, B - max weight
def knapsack(W: list, P: list, B: int) -> int:
    n = len(W)
    F = [[0 for _ in range(B + 1)] for _ in range(n)]

    for b in range(W[0], B + 1):
        F[0][b] = P[0]

    for b in range(B + 1):
        for i in range(1, n):
            F[i][b] = F[i - 1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])

    items = []

    def get_items(i: int, b: int) -> None:
        if i == 0:
            if b >= W[0]:
                items.append(i)
            return

        if F[i][b] != F[i - 1][b]:
            items.append(i)
            get_items(i - 1, b - W[i])
        else:
            get_items(i - 1, b)

    get_items(n - 1, B)
    print(f"Used items: {items}")

    return F[n - 1][B]


# test and odtworzenie

# W = [3, 4, 6, 5]
# P = [2, 3, 1, 4]
# B = 8


W = [10, 20, 30]
P = [60, 100, 120]
B = 50
print(knapsack(W, P, B))
