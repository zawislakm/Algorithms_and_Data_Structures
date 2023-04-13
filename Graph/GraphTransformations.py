def list_to_matrix(G: list) -> list:
    n = len(G)
    G_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in G[i]:
            G_matrix[i][j] = 1
    return G_matrix


def matrix_to_list(G: list) -> list:
    n = len(G)
    G_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] == 1:
                G_list[i].append(j)
    return G_list


def list_to_matrix_wages(G: list) -> list:
    n = len(G)
    G_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j, u in G[i]:
            G_matrix[i][j] = u
    return G_matrix


def matrix_to_list_wages(G: list) -> list:
    n = len(G)
    G_list = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j] > 0:
                G_list[i].append((j, G[i][j]))
    return G_list
