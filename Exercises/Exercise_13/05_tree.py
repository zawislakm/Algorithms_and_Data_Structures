"""
Find value of maximal path in tree
"""

"""
Go down on tree till leafs. Find maximal paths from each node down. When node have atleast two children sum two maximal
path from this root. Then pick maximal value from path under node and path as root to path.
"""


def tree(T: list, n: int, s: int = 0):
    G = [[] for _ in range(n)]

    for u, v, w in T:
        G[u].append((v, w))

    max_path_under = [-1 for _ in range(n)]  # node where path ends
    max_path_root = [-1 for _ in range(n)]  # root where path comes from down and go down again

    def rek(u: int) -> int:

        if not G[u]:
            return 0

        leafs = []
        for v, p in G[u]:
            leafs.append(p + rek(v))

        if len(leafs) > 1:
            leafs.sort(reverse=True)
            max_path_root[u] = leafs[0] + leafs[1]

        max_path_under[u] = max(leafs)

        return max(leafs)

    rek(s)

    return max(max(max_path_root), max(max_path_under))


T = [(0, 1, -7), (0, 7, 8), (1, 2, 3), (1, 3, 2), (1, 4, 1), (2, 5, -4), (2, 6, 10), (7, 8, -5), (7, 9, 4), (8, 10, 4),
     (8, 11, 10), (4, 12, -50), (12, 13, 100)]
nodes = 14
print(tree(T, nodes))
