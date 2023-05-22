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


def egde_list_to_list(G: list) -> list:
    n = -1
    for u, v, _ in G:
        n = max(n, u, v)
    n += 1
    G_list = [[] for _ in range(n)]

    for u, v, w in G:
        G_list[u].append((v, w))
        G_list[v].append((u, w))
    return G_list


def list_to_edge_list(G: list) -> list:
    G_edge = []
    n = len(G)
    for u in range(n):
        for v, p in G[u]:
            if v > u:
                G_edge.append((u, v, p))
    return G_edge


def edge_list_to_matrix(G: list) -> list:
    n = -1
    for u, v, _ in G:
        n = max(n, u, v)
    n += 1
    G_matrix = [[0 for _ in range(n)] for _ in range(n)]

    for u, v, p in G:
        G_matrix[u][v] = p
        G_matrix[v][u] = p

    return G_matrix


def matrix_to_edge_list(G: list) -> list:
    n = len(G)
    G_edge = []

    for u in range(n):
        for v in range(n):
            if v > u and G[u][v] != 0:
                G_edge.append((u, v, G[u][v]))
    return G_edge
