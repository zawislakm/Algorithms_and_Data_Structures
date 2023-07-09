from egz2btesty import runtests


# O(n) solution
def magic(C: list) -> int:
    # tu prosze wpisac wlasna implementacje

    n = len(C)
    cave = [-1 for _ in range(n)]
    cave[0] = 0

    for i in range(n):
        g = C[i][0]
        if cave[i] == -1:
            continue
        for cost, door in C[i][1:]:
            if g - cost <= 10 and door != -1:
                cave[door] = max(cave[door], g + cave[i] - cost)

    return cave[-1]


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(magic, all_tests=True)
C = [[8, [6, 3], [4, 2], [7, 1]],  # 0
     [22, [12, 2], [21, 3], [0, -1]],  # 1
     [9, [11, 3], [0, -1], [7, -1]],  # 2
     [15, [0, -1], [1, -1], [0, -1]]]  # 3

magic(C)
