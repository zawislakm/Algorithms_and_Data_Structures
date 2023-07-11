import math

"""
file_ready array oznaczna ile jeszcze trzeba jakis zaleznosci zainstlowac zanim bedzie mozna zaisntalowac
dany plik

start array przechowuje dwie tablice, na indexie zero takie wiercholki które mozna zainstloawc
majac wlozna dyskietke A, a na indexie B takie jaki gdy jest wloznona dyskietka B

G odwraca tak jakby zaleznosci wiec, wskazuje jakie zaloznosci moga sie  odblokowujac  
po zainstlowaniu danego pliku


Ponizsze wykonuje sie dwa razy, raz zaczynajac od wartosci A, raz dla wartosci B.

DFS zaczyna od zadnego wierzcholka, przechodzi po sasiednich wierzcholkach i zmniejsza
wartosci z file_ready array, jezeli nie trzeba juz nic instlowac to sprawdza czy jest odpowiednia dyskietka
wsadzona, jezeli tak to ponowanie odpala sie dfs, jezeli nie to dodawne jest to odpowedniej tablicy start
dla przeciwnej dyskietki. Na przemian odpalane sa wiercholki z dyskietki A oraz B. Kazde wykonanie 
petli liczy sie jako zmiane dyskietki. 
"""
from kolutesty import runtests


def swaps(disk, depends):
    n = len(disk)

    file_ready_A = [0 for _ in range(n)]
    file_ready_B = [0 for _ in range(n)]

    startA = [[], []]
    startB = [[], []]

    G = [[] for _ in range(n)]

    for i, H in enumerate(depends):
        nh = len(H)
        file_ready_A[i] = file_ready_B[i] = nh

        if nh == 0:
            if disk[i] == 'A':
                startA[0].append(i)
                startB[0].append(i)
            else:
                startA[1].append(i)
                startB[1].append(i)
        else:
            for j in H:
                G[j].append(i)

    def DFS_visit(u, start, file_ready, flag):
        nonlocal depends
        for v in G[u]:
            file_ready[v] -= 1
            if file_ready[v] == 0:
                if disk[u] == disk[v]:
                    DFS_visit(v, start, file_ready, flag)
                else:
                    start[flag].append(v)

    sumA = sumB = -1
    if startA[0]:
        while startA != [[], []]:
            if startA[0]:
                for u in startA[0]:
                    DFS_visit(u, startA, file_ready_A, 1)
                startA[0] = []
            elif startA[1]:
                for u in startA[1]:
                    DFS_visit(u, startA, file_ready_A, 0)
                startA[1] = []
            sumA += 1
    else:
        sumA = math.inf

    if startB[1]:
        while startB != [[], []]:
            if startB[1]:
                for u in startB[1]:
                    DFS_visit(u, startB, file_ready_B, 0)
                startB[1] = []
            elif startB[0]:
                for u in startB[0]:
                    DFS_visit(u, startB, file_ready_B, 1)
                startB[0] = []
            sumB += 1
    else:
        sumB = math.inf

    print(f'SumA: {sumA}, SumB: {sumB}')
    return min(sumB, sumA)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(swaps, all_tests=True)

disk = ['A', 'A', 'B', 'B']
depends = [[2, 3], [], [1, 3], [1]]
print(swaps(disk, depends))
