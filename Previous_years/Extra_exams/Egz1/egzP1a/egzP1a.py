import math

from egzP1atesty import runtests

"""
F(i) = minmalna ilosc potrzeban to zbudowania napisu dlugosci i dla i > 0
F(0) = 1 dla i == 0
F(i) = 0 dla i < 0
"""


def titanic(W: str, M: list, D: list) -> int:
    # tutaj proszę wpisać własną implementację
    # print(W,D)
    R = ''
    for s in W:
        for l, d in M:
            if s == l:
                R += d
                break
    n = len(R)
    DP = [math.inf for _ in range(n + 1)]
    DP[0] = 0
    DP[1] = 1
    P = []
    for i in D:
        P.append(M[i][1])

    for i in range(1, n):
        for s in P:
            if len(s) <= i + 1 and s == R[i - len(s) + 1:i + 1]:
                DP[i + 1] = min(DP[i + 1], DP[i - len(s) + 1] + 1)
        # break

    # print(f'Messege: {R}')
    # print(f'Letters: {P}')
    # print(DP)
    return DP[n]


runtests(titanic, recursion=False)

M = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'), ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
     ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'), ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
     ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'), ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
     ('Y', '-.--'), ('Z', '--..')]
W = 'SOS'
D = [0, 4, 13, 19, 25]

W1 = 'BGTILCLEXI'
D1 = [0, 2, 4, 13, 17, 19]
titanic(W, M, D)
