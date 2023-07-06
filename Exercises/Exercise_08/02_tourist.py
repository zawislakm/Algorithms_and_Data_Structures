"""
Petrol stations. Tourist want to travel from city A to city B with the lowest possible cost. Each edges have weight.
On every vertex is petrol station with own oil cost. Find the cheapest path. Car tank have a given limit D to tank.
"""

"""
Modified dijkstra algorythem. Each vertex is multiple by d+1 (size of car tank).
"""

import queue

INF = 10 ** 10


def tourist(G: list, s: int, t: int, d: int) -> int:
    n = len(G)
    visited = [[False for _ in range(d + 1)] for _ in range(n)]
    weights = [[INF for _ in range(d + 1)] for _ in range(n)]
    parents = [[[-1, -1] for _ in range(d + 1)] for _ in range(n)]
    Q = queue.PriorityQueue()
    weights[s][0] = 0
    visited[s][0] = True
    Q.put((0, 0, s))  # weight, petrol, vertice
    while not Q.empty():
        w, oil_tank, u = Q.get()

        elem_list, oil_cost = G[u]

        for v, p in elem_list:
            oil_bought = 0
            while oil_bought + oil_tank <= d:

                if oil_bought + oil_tank >= p:

                    oil_next_stop = oil_bought + oil_tank - p
                    if visited[v][oil_next_stop] is False and weights[v][oil_next_stop] > w + oil_bought * oil_cost:
                        weights[v][oil_next_stop] = w + oil_bought * oil_cost
                        parents[v][oil_next_stop] = [u, oil_tank]
                        Q.put((w + oil_bought * oil_cost, oil_next_stop, v))

                oil_bought += 1

        visited[u][oil_tank] = True

    min_index = weights.index(min(weights))
    vertex_pointer, oil_pointer = parents[t][min_index]

    path = []

    while vertex_pointer != -1 and oil_pointer != -1:
        path.append(vertex_pointer)
        vertex_pointer, oil_pointer = parents[vertex_pointer][oil_pointer]

    path.reverse()
    print(f'Found cheapest path is {path} with oil cost equal {weights[t][min_index]}')

    return min(weights[t])


graph = [[[(1, 5), (2, 3)], 8],
         [[(0, 5), (2, 3), (3, 5)], 5],
         [[(0, 3), (1, 3), (3, 4), (5, 1)], 3],
         [[(1, 5), (2, 4), (4, 6)], 3],
         [[(3, 6)], 1],
         [[(2, 1)], 1]]

s = 0
t = 4
d = 6
tourist(graph, s, t, d)
