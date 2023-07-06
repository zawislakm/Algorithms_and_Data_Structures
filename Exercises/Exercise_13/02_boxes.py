"""
List of falling boxes, find which boxes need to be removed to make the next falling boxes fit on top of the previous boxes
Find minimal number boxes to remove. Boxes fall in given order
"""

# LIS
"""
#LIS idea
Simple find which boxes pick to build highest tower

F(i) = the length of the height tower of blocks ending on i index
"""


def boxes(B: list):
    n = len(B)
    F = [1 for _ in range(n)]
    P = [-1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            if B[j][0] <= B[i][0] and B[i][1] <= B[j][1]:
                P[i] = j
                F[i] = F[j] + 1

    def find_tower(i: int):
        nonlocal path
        if P[i] != -1:
            find_tower(P[i])
        path.append(B[i])

    path = []

    find_tower(F.index(max(F)))

    print(f'Found solution is: {path}, height: {max(F)}')


B = [(0, 4), (1, 4), (3, 5), (5, 6), (1, 3), (2, 3)]
boxes(B)
