# W - weight, P - price, B - max weight
# constant version
# greedy


def knapsack(W: list, P: list, B: int) -> int:
    total = 0

    H = []
    for w, p in zip(W, P):
        H.append((p / w, w))
    H.sort(key=lambda x: x[0], reverse=True)

    print(H)
    i = 0
    while B > 0 and i < len(H):
        p, w = H[i]
        total += p * min(B, w)
        B -= min(B,w)
        i += 1

    return total


W = [3, 4, 6, 5]
P = [2, 3, 1, 4]
B = 8

print(knapsack(W, P, B))
