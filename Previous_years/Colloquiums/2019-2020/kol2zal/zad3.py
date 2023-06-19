from zad3testy import runtests


def Dijkstra(G:list,s:int,t:int) -> int:
    n = len(G)
    visited = [False for _ in range(n)]
    weight = [float('inf') for _ in range(n)]

    weight[s] = 0

    for _ in range(n):

        u = -1
        low = float('inf')
        for v in range(n):
            if visited[v] is False and low > weight[v]:
                low = weight[v]
                u = v
        visited[u] = True

        for v in range(n):
            if visited[v] is False and weight[v] > weight[u] + G[u][v] and G[u][v] > 0:
                weight[v] = weight[u] + G[u][v]



    if weight[t] == float('inf'):
        return -1
    return weight[t]

def connceted(num1:int,num2:int) -> bool:
    num1 = str(num1)
    num2 = str(num2)

    for i in num1:
        if i in num2:
            return True
    return False


def find_cost(P):
    # tu prosze wpisac wlasna implementacje
    n = len(P)
    G = [[0 for _ in range(n)] for _ in range(n)]

    s = -1
    t = -1

    low = float('inf')
    high = -100

    for i in range(n):
        num1 = P[i]
        for j in range(i+1,n):
            num2 = P[j]
            if connceted(num1,num2):
                G[i][j] = G[j][i] = abs(num1-num2)
        if num1 > high:
            t = i
            high = num1
        if num1 < low:
            s = i
            low = num1


    return Dijkstra(G,s,t)

runtests(find_cost)

# T = [123, 890, 688, 587, 257, 246]
#
# find_cost(T)



