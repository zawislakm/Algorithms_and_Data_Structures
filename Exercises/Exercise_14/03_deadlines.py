"""
Set of tasks T = {t1,...tn}. Each task additionally has:
- execution deadline, d (nautral number)
- profit from execution on time, g (natural number).

The execution of each task takes a unit of time. If the task t is completed before it exceeds its
time limit, we get a reward for it. (The first selected task is performed at time 0. the second selected task
at time 1, the third at time 2). Find a subset of tasks that can be completed on time and leads to maximum profit.


"""

"""
Greedy
Which task can we do last?
All tasks begin simultaneously
Analyze deadlines from the end, take the task that gives the highest profit
"""

INF = 10 ** 10


def deadlines(D: list, G: list) -> (list, int):
    used = [False for _ in range(len(D))]
    n = max(D)
    done = []
    gold = 0

    for dead in range(n, -1, -1):

        best = index = -1

        for i in range(len(D)):
            if D[i] >= dead and used[i] is False and best < G[i]:
                best = G[i]
                index = i

        if best != -1:
            done.append(index)
            print(G[index])
            used[index] = True
            gold += best

    return done, gold


D = [5, 1, 2, 4, 5, 3, 2]
G = [10, 1, 9, 7, 5, 3, 4]
deadlines(D, G)
