"""
Traktor jedzie z punktu A do punktu B. Spalanie traktora to dokładnie jeden litr paliwa na jeden kilometr trasy.
W baku miesci sie dokładnie L litrów paliwa. Trasa z A do B to prosta, na której znajdują sie stacje benzynowe
(na pozycjach bedących liczbami naturalanymi; A jest na pozycji 0).

Zadania:
1. Wyznaczamy stacje na których tankujemy tak, zeby łączna liczba tankowań była minimalana
2. Wyznaczamy stacje tak, zeby koszt przejazdu był minimalny ( w tym przypadku kazda stacja ma dodaktowo cene
za litr paliwa). Na kazdej stacji mozemy tankować dowolna ilosc paliwa.
3. Podobnie jak w zadaniu 2. lecz teraz na stacji trzeba tankować do pełna
"""
import math
import queue

"""
1. Greedy, looking from petrol station in range L to 1, tractor stops on to furthers possible station
2. Greedy possible, used Dijkstra
3. Dynamic, F(x,i) - koszt jazdy z 0 do i maja x paliwa (na początku trasy)
x - ile zostało jeszcze paliwa
i - pozycja do której chcemy dojeach
"""


def task1(P: list, A: int, B: int, L: int) -> list:
    stops = []

    w = 0

    while w + L < B:

        for i in range(w + L, w, -1):
            if P[i] != 0:
                w = i
                stops.append(i)
                break
        else:
            print(f'Impossible to reach point B')
            return []

    print(f'Tractor stops on {stops} stations')
    return stops


def task2(P: list, A: int, B: int, L: int) -> (int, list):
    n = len(P)
    G = [[] for _ in range(n)]
    P[B] = -1
    for i in range(n - 1):
        if P[i] != 0:
            for j in range(i + 1, min(i + L + 1, n)):
                if P[j] != 0:
                    dis = j - i
                    G[i].append((j, P[i] * dis))

    visited = [False for _ in range(n)]
    weights = [math.inf for _ in range(n)]
    parent = [None for _ in range(n)]
    Q = queue.PriorityQueue()
    weights[A] = 0
    Q.put((0, A))

    while not Q.empty():
        w, u = Q.get()

        for v, p in G[u]:
            if visited[v] is False and weights[v] > w + p:
                weights[v] = w + p
                parent[v] = u
                Q.put((w + p, v))
        visited[u] = True

    if visited[B] is True:
        path = []
        ptr = B
        while ptr is not None:
            path.append(ptr)
            ptr = parent[ptr]
        path.reverse()
        print(f'Tracktor paid {weights[B]} for the road, stopping on {path}')
        return weights[B], path
    return None


oil = [3, 0, 2, 0, 7, 0, 10, 0, 2, 1, 0, 0]
A = 0
B = 11
L = 4
task1(oil, A, B, L)
